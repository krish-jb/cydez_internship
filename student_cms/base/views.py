from django.shortcuts import render, redirect
from .form import StudentDetailsForm
from .models import Student

# Create your views here.


def student_list(request):
    context = {
        "student_list_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "add_student_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "edit_or_add": "Add Student",
        "students": Student.objects.all(),
    }
    return render(request, "base/student_list.html", context)


def add_student(request):
    context = {
        "student_list_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "add_student_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "edit_or_add": "Add Student",
        "heading": "Student Details",
        "sub_heading": "Enter studnet detail in below form. This will be uploaded to University database.",
    }

    if request.method == "POST":
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_student")
    else:
        form = StudentDetailsForm()
        context["form"] = form

    return render(request, "base/student_form.html", context)


def update_student(request, pk):
    student_details = Student.objects.get(id=pk)
    context = {
        "student_list_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "add_student_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "edit_or_add": "Edit Student",
        "heading": "Update Student Details",
        "sub_heading": "Update the student's details using the form below. Changes will be reflected in the university database.",
        "form": StudentDetailsForm(instance=student_details),
    }

    if request.method == "POST":
        form = StudentDetailsForm(request.POST, instance=student_details)
        if form.is_valid():
            form.save()
            return redirect("list_student")

    return render(request, "base/student_form.html", context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect("list_student")
