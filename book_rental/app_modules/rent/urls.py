from django.urls import path
from app_modules.rent import views

app_name = "rent"

urlpatterns = [
    path('', views.ListRentBookView.as_view(), name="rent_book_list"),
    path('ajax/', views.ListRentBookAjaxView.as_view(), name="rent_book_list_ajax"),
    path('create/', views.RentBookView.as_view(), name="rent_book"),
    path('return/<int:pk>/', views.ReturnRentBookView.as_view(), name="return_rent_book"),
]
