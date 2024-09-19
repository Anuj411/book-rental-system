
from django import forms
from app_modules.student.models import Student

class StudentForm(forms.ModelForm):
    image = forms.ImageField(label="Image")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20)
    full_name = forms.CharField(label="Full Name", max_length=100)

    class Meta:
        model = Student
        fields = ("student_id", "email", "full_name", "image", "phone", "department", "degree", "college_email", 'semester')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label
        
        self.fields["image"].required = False
    