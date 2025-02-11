from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name="list_book"),
    path('add-book', views.add_book, name="add_book"),
    path('update-book-details/<str:pk>', views.update_book, name="update_book"),
    path('delete-book/<str:pk>', views.delete_book, name="delete_book")
]