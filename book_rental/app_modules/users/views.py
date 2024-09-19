from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app_modules.users.forms import UpdateProfileForm
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        if self.request.user.role in [User.SUPER_ADMIN, User.ADMIN]:
            return "users/admin/dashboard.html"
        elif self.request.user.role in User.STUDENT:
            return "users/student/dashboard.html"
        return "404.html"


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = "users/profile-update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.image:
            context["image"] = self.object.image.url
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("users:dashboard"))