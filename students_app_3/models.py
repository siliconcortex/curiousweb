from django.db import models
from django.utils import timezone
from django.urls import reverse
from main_app.models import User
from exams_app.models import ExamTicket

class Subjects(models.Model):
    name = models.CharField(max_length = 100)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Student(models.Model):
    #this is student for ECE, however, the specificities have been
    #removed so that the app becomes reusable
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name = 'students_app_3_user')
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    birthdate = models.DateField() #this is required
    address = models.TextField(max_length = 1000)
    religion = models.CharField(max_length = 50, blank = True)
    mobile_number = models.CharField(max_length = 100)
    facebook_username = models.CharField(max_length = 100, blank= True)
    email = models.EmailField()
    gender = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)

    first_name_contact_person = models.CharField(max_length=100)
    last_name_contact_person = models.CharField(max_length=100)
    middle_name_contact_person = models.CharField(max_length=100, blank = True)
    address_contact_person = models.CharField(max_length=1000)
    mobile_number_contact_person = models.CharField(max_length = 1000)

    id_picture = models.ImageField(blank = True, upload_to = 'students_app_3/id')
    payment_picture = models.ImageField(upload_to = 'students_app_3/payment')

    def get_absolute_url(self):
        return reverse("students_app_3:detail",kwargs={'pk':self.pk})
