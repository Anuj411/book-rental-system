
from django import forms
from app_modules.rent.models import Rent
from datetime import datetime

class RentBookForm(forms.ModelForm):

    class Meta:
        model = Rent
        fields = ("student", "check_in_date")
        widgets={
            'check_in_date' : forms.TextInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label
        
        self.fields["check_in_date"].initial = datetime.today().date()



class ReturnRentBookForm(forms.ModelForm):

    class Meta:
        model = Rent
        fields = ("check_out_date",)
        widgets={
            'check_out_date' : forms.TextInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label
        
        self.fields["check_out_date"].required = True
        