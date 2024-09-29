from django.urls import path
from app_modules.student import views

app_name = "students"

urlpatterns = [
    path('', views.ListStudentView.as_view(), name="student_list"),
    path('ajax/', views.ListStudentAjaxView.as_view(), name="student_list_ajax"),
    path('create/', views.CreateStudentView.as_view(), name="student_create"),
    path('<int:pk>/details/', views.StudentRentedBookView.as_view(), name="student_rented_book"),
]
