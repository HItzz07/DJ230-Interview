from django.urls import path
from .import views

urlpatterns = [
    path("",views.index),
    path("/books", views.get_books, name="get-books"),
    path("/members", views.get_members, name="get-members"),
    path("/checkout_book", views.checkout_book, name="checkout-book"),
    path("/return_book", views.return_book, name="return-book"),
    path("/reserve_book", views.reserve_book, name="reserve-book"),
]
