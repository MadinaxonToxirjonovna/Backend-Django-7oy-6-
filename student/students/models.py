from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
