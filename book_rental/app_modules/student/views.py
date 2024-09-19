from calendar import month
from datetime import datetime
from django.views.generic import ListView, CreateView, View, DetailView
from app_modules.student.models import Student
from app_modules.student.forms import StudentForm

from django_datatables_too.mixins import DataTableMixin
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from app_modules.base.permissions import AdminLoginRequiredMixin

from app_modules.users.models import User


class ListStudentView(AdminLoginRequiredMixin, ListView):
    model = Student
    template_name = "student/student-list.html"


class ListStudentAjaxView(DataTableMixin, View):
    model= Student
    
    def get_queryset(self):
        degree = self.request.GET.get("degree")
        department = self.request.GET.get("department")
        sem = self.request.GET.get("sem")
        
        qs = Student.objects.all()
        if degree:
            qs = qs.filter(degree = degree)
        
        if department:
            qs = qs.filter(department = department)
        
        if sem:
            qs = qs.filter(semester = sem)

        return qs.order_by("-id")

    def filter_queryset(self, qs):
        """Return the list of items for this view."""

        if self.search:
            return qs.filter(
                Q(user__full_name__icontains=self.search)
            )
        return qs

    def get_actions(self, obj):
        url = reverse("students:student_rented_book", kwargs={"pk": obj.id})
        return f'<div class="row"><center><a href="{url}"><button class="btn btn-primary">View books</button></a></center></div>'

    def prepare_results(self, qs):
        return [
            {
                'id': o.id,
                'user__full_name': o.user.full_name,
                'student_id': o.student_id,
                'department': o.department,
                'college_email': o.college_email,
                'degree': o.degree,
                'semester': o.semester,
                'actions': self.get_actions(o),
            }
            for o in qs
        ]

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


class CreateStudentView(AdminLoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student-create.html"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        full_name = form.cleaned_data["full_name"]
        image = form.cleaned_data["image"]
        phone = form.cleaned_data["phone"]
        today_date = datetime.today().date()

        instance = form.save(commit=False)

        new_user = User(email=email, full_name=full_name, image=image, role=User.STUDENT, phone=phone)
        new_user.username = email.split("@")[0] + str(today_date.day) + str(today_date.month) + str(today_date.year)
        new_user.save()

        instance.user = new_user
        instance.save()
        return HttpResponseRedirect(reverse("students:student_list"))

    def form_invalid(self, form):
        return super().form_invalid(form)


class StudentRentedBookView(DetailView):
    model = Student
    template_name = "student/student-details.html"
    