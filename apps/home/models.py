from tokenize import group
from django.db import models

# Create your models here.


class Advisor(models.Model):
    fname = models.CharField(max_length=30, null=True, blank=True)
    mname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length=30, null=True, blank=True)
    department = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.fname


class Student(models.Model):
    fname = models.CharField(max_length=30, null=True, blank=True)
    mname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length=30, null=True, blank=True)
    studentid = models.CharField(max_length=30, null=True, blank=True)
    section = models.IntegerField(null=True, blank=True)
    group = models.IntegerField(null=True, blank=True)
    advisor = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.studentid
