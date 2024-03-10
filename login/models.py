#models.py
from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Note: In production, use a more secure way to store passwords, such as hashing.

    def __str__(self):
        return self.username


class Tutor(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    education_qualification_1 = models.CharField(max_length=100)
    education_qualification_2 = models.CharField(max_length=100)
    education_qualification_3 = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    experience = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)  # You might want to use a more secure way to store passwords

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
