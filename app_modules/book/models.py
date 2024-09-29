from django.db import models
from app_modules.base.models import BaseModel


class Book(BaseModel):
    title = models.CharField("Title", max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.CharField("Author", max_length=200, null=True, blank=True)
    no_of_pages = models.IntegerField("No of Pages")

    def __str__(self):
        return self.title
    
    @property
    def get_monthly_rental_charge(self):
        return self.no_of_pages / 100
    