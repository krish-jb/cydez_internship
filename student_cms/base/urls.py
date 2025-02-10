from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name="list_student"),
    path('add-student', views.add_student, name="add_student"),
    path('update-student-details/<str:pk>', views.update_student, name="update_student"),
    path('delete-student/<str:pk>', views.delete_student, name="delete_student")
]