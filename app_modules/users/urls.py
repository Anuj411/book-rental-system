from django.urls import path
from app_modules.users import views

app_name = "users"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('update/profile/<int:pk>', views.UpdateProfileView.as_view(), name="update_profile"),
]

handler404 = "app_modules.users.views.handler404"
handler403 = "app_modules.users.views.handler403"