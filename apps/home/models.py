from tokenize import group
from django.db import models

# Create your models here.


class Advisor(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    school = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    studentid = models.CharField(max_length=30, null=True, blank=True)
    section = models.IntegerField(null=True, blank=True)
    program = models.CharField(max_length=30, null=True, blank=True)
    advisor = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.studentid
