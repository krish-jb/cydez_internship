from django.forms import ModelForm
from django import forms
from .models import Book

class BookDetailsForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book_name", "author_name", "price", "shelf", "borrowed_by"]
        tailwind_classes = "block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": tailwind_classes}),
            "author_name": forms.TextInput(attrs={"class": tailwind_classes}),
            "price": forms.NumberInput(attrs={"class": tailwind_classes, "min": 0}),
            "shelf": forms.TextInput(attrs={"class": tailwind_classes}),
            "borrowed_by": forms.TextInput(attrs={"class": tailwind_classes}),
        }
        
    def label_tag(self, name, label=None, attrs=None, label_suffix=None):
        attrs = attrs or {}
        attrs['class'] = "block text-sm/6 font-semibold text-gray-900"
        return super().label_tag(name, label, attrs, label_suffix)
        