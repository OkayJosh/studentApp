from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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

    def __str__(self):
        return '%s' % (self.name)

class Book(models.Model):
    owned_by = models.ForeignKey(Student, related_name="has_books", on_delete=models.CASCADE, 
                         null=True, blank=True)
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255, null=True, default="ISBN")
    purpose = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '%s for %s' % (self.name, self.owned_by)

class Literacy(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    literacy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default="3")
    describe_literacy = models.TextField("Describe the Literacy of the Student", null=True)

    def __str__(self):
        return self.literacy

class Numeracy(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    numeracy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    describe_numeracy = models.TextField("Describe the Literacy of the Student", null=True)

    def __str__(self):
        return 'Numeracy details for %s' % (self.student)

class Attendance(models.Model):

    # Many attendance will belong to one student
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    present = models.BooleanField()

    def __str__(self):
        return '%s is %s' % (self.student, self.present)

class Incentive(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    description_of_incentive = models.TextField("Describing the incentives", null=True)
    date_of_inclusion = models.DateField(null=True)

class Appraisal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField("Name of Appraisal",max_length=255, null=True)
    method_of_appraisal = models.CharField(max_length=255, null=True)
    performance = models.TextField("Describing the Performance of the student", null=True)
    brief = models.TextField()

    def __str__(self):
        return '%s' % (self.name)
    
class Posting(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    #school = models.ForeignKey(School ,on_delete=models.CASCADE, null= True, related_name='studentPosting', blank=True)
    date_of_posting = models.DateField("Date of Posting")

    def __str__(self):
        return '%s posted to %s' % (self.student, self.school)