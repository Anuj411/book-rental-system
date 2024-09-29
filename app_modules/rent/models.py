from django.db import models

from app_modules.base.models import BaseModel
from app_modules.book.models import Book
from app_modules.student.models import Student

from datetime import datetime, timedelta


class Rent(BaseModel):
    PENDING = "Pending"
    RETURNED = "Returned"

    STATUS = (
        (PENDING, "pending"),
        (RETURNED, "returned"),
    )

    book = models.ForeignKey(Book, related_name="students", on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, related_name="rented_books", on_delete=models.CASCADE)
    check_in_date = models.DateField("Checkin Date")
    check_out_date = models.DateField("Checkout Date", null=True, blank=True)
    total_charges = models.DecimalField("Total Changes ($)", max_digits=20, decimal_places=2, default=0.00)
    status = models.CharField("Status", choices=STATUS, max_length=100, default=PENDING)

    def __str__(self):
        return self.book.title
    
    @property
    def calculate_rent_book_charges(self):
        # Assumed 1 month = 30 days

        if self.status == Rent.PENDING:
            today_date = datetime.today().date()

            if today_date > self.check_in_date:
                charged_days = today_date - self.check_in_date
                rent_months = charged_days.days // 31
                total_charges = rent_months * self.book.get_monthly_rental_charge
                return total_charges
        else:
            if self.check_out_date:
                return self.total_charges
        return 0
    