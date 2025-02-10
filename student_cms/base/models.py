from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mark_subject_1 = models.IntegerField()
    mark_subject_2 = models.IntegerField()
    mark_subject_3 = models.IntegerField()
    total_mark = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.total_mark = (
            self.mark_subject_1 + self.mark_subject_2 + self.mark_subject_3
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
