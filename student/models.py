from django.db import models

from django.contrib.auth.models import User


class Student(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                        null=True)
    name = models.CharField(max_length=300)
    pics = models.ImageField(default='default.jpg')
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    local_government_origin = models.CharField(max_length=20,
                         null=True, default='local origin')
    state_origin = models.CharField(max_length=20, null=True, 
                        default='state origin')
    local_government_residence = models.CharField(max_length=20, 
                        null=True, default='local residence')
    state_residence = models.CharField(max_length=20, null=True, 
                        default='state residence')
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.name

class Parent(models.Model):

    student = models.OneToOneField(Student, on_delete=models.CASCADE, 
                    related_name="has_parent", primary_key=True)
    name = models.CharField(max_length=300)
    pics = models.ImageField(default='default.jpg')
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    local_government_origin = models.CharField(max_length=20, null=True)
    state_origin = models.CharField(max_length=20, null=True)
    local_government_residence = models.CharField(max_length=20, 
                        null=True)
    state_residence = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

class Book(models.Model):
    owned_by = models.ForeignKey(Student, on_delete=models.CASCADE, 
                        related_name="has_books", null=True, blank=True)
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255, null=True, default="ISDN")
    purpose = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '%s for %s' % (self.name, self.student)