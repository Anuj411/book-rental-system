
from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", "full_name", "image", "phone", "role")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label
        
        self.fields["role"].disabled = True
        self.fields["email"].widget.attrs["readonly"] = True
        self.fields["image"].required = False