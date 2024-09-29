from django.views.generic import CreateView, View, ListView, UpdateView
from app_modules.rent.models import Rent

from app_modules.rent.forms import RentBookForm, ReturnRentBookForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q
from app_modules.base.permissions import AdminLoginRequiredMixin

from app_modules.book.models import Book


class ListRentBookView(AdminLoginRequiredMixin, ListView):
    model = Rent
    template_name = "rent/rent-list.html"


class ListRentBookAjaxView(DataTableMixin, View):
    model= Rent
    
    def get_queryset(self):
        qs = Rent.objects.all()
        student_id = self.request.GET.get("student")

        if student_id:
            qs = qs.filter(student__id = student_id)
            
        return qs.order_by("-id")

    def filter_queryset(self, qs):
        """Return the list of items for this view."""

        if self.search:
            return qs.filter(
                Q(book__title__icontains=self.search)
            )
        return qs
    
    def get_actions(self, obj):
        if obj.status == Rent.PENDING:
            url = reverse("rent:return_rent_book", kwargs={"pk": obj.id})
            return f'<div class="row"><center><a href="{url}"><button class="btn btn-primary">Return</button></a></center></div>'
        else:
            return "-"
        
    def prepare_results(self, qs):
        return [
            {
                'id': o.id,
                'student__student_id': o.student.student_id,
                'student__user__full_name': o.student.user.full_name,
                'check_in_date': o.check_in_date,
                'check_out_date': o.check_out_date if o.check_out_date else "-",
                'book__title': o.book.title,
                "rent_charges": o.calculate_rent_book_charges,
                "status": o.status,
                "actions": self.get_actions(o),
            }
            for o in qs
        ]

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


class RentBookView(AdminLoginRequiredMixin, CreateView):
    form_class = RentBookForm
    template_name = "rent/rent-new-book.html"

    def form_valid(self, form):
        title = form.data["title"]
        author = form.data["author"]
        no_of_pages = form.data["no_of_pages"]

        new_book = Book(title = title, author = author, no_of_pages = no_of_pages)
        new_book.save()

        instance = form.save(commit=False)
        instance.book = new_book
        instance.save()

        return HttpResponseRedirect(reverse("rent:rent_book_list"))

    def form_invalid(self, form):
        return super().form_invalid(form)


class ReturnRentBookView(AdminLoginRequiredMixin, UpdateView):
    model = Rent
    form_class = ReturnRentBookForm
    template_name = "rent/return-rent-book.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = Rent.RETURNED
        instance.save()

        if instance.check_out_date > instance.check_in_date:
            charged_days = instance.check_out_date - instance.check_in_date
            rent_months = charged_days.days // 31
            total_charges = rent_months * instance.book.get_monthly_rental_charge
            
            instance.total_charges = total_charges
            instance.save()
        return HttpResponseRedirect(reverse("rent:rent_book_list"))

    def form_invalid(self, form):
        return super().form_invalid(form)
