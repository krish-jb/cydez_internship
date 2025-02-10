from django.forms import ModelForm
from django import forms
from .models import Student

class StudentDetailsForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "student_class", "email", "mark_subject_1", "mark_subject_2", "mark_subject_3"]
        tailwind_classes = "block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": tailwind_classes}),
            "last_name": forms.TextInput(attrs={"class": tailwind_classes}),
            "student_class": forms.TextInput(attrs={"class": tailwind_classes}),
            "email": forms.EmailInput(attrs={"class": tailwind_classes}),
            "mark_subject_1": forms.NumberInput(attrs={"class": tailwind_classes, "max": 100, "min": 0}),
            "mark_subject_2": forms.NumberInput(attrs={"class": tailwind_classes, "max": 100, "min": 0}),
            "mark_subject_3": forms.NumberInput(attrs={"class": tailwind_classes, "max": 100, "min": 0}),
        }
        
    def label_tag(self, name, label=None, attrs=None, label_suffix=None):
        attrs = attrs or {}
        attrs['class'] = "block text-sm/6 font-semibold text-gray-900"
        return super().label_tag(name, label, attrs, label_suffix)
        