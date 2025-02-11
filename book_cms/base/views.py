from django.shortcuts import render, redirect
from .form import BookDetailsForm
from .models import Book

# Create your views here.


def book_list(request):
    context = {
        "book_list_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "add_book_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "edit_or_add": "Add Book",
        "books": Book.objects.all(),
    }
    return render(request, "base/book_list.html", context)


def add_book(request):
    context = {
        "book_list_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "add_book_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "edit_or_add": "Add Book",
        "heading": "Book Details",
        "sub_heading": "Enter studnet detail in below form. This will be uploaded to University database.",
    }

    if request.method == "POST":
        form = BookDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_book")
    else:
        form = BookDetailsForm()
        context["form"] = form

    return render(request, "base/book_form.html", context)


def update_book(request, pk):
    book_details = Book.objects.get(id=pk)
    context = {
        "book_list_class": "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
        "add_book_class": "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
        "edit_or_add": "Edit Book",
        "heading": "Update Book Details",
        "sub_heading": "Update the book details using the form below. Changes will be reflected in the library database.",
        "form": BookDetailsForm(instance=book_details),
    }

    if request.method == "POST":
        form = BookDetailsForm(request.POST, instance=book_details)
        if form.is_valid():
            form.save()
            return redirect("list_book")

    return render(request, "base/book_form.html", context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("list_book")
