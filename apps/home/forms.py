from distutils.fancy_getopt import FancyGetopt
from tokenize import group
from django import forms
from django.forms import ModelForm
from .models import Student, Advisor


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ), required=False)
    mname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle Name",
                "class": "form-control"
            }
        ), required=False)
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ), required=False)
    studentid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Student Id",
                "class": "form-control"
            }
        ), required=False)
    section = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Section",
                "class": "form-control"
            }
        ), max_value=100, min_value=1, required=False)
    group = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Group",
                "class": "form-control"
            }
        ), max_value=200, min_value=1, required=False)


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    mname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle Name",
                "class": "form-control"
            }
        ))
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Department",
                "class": "form-control"
            }
        ))
    
    
    
class AssignForm(ModelForm):
    class Meta:
        model = Student
        fields = ('advisor',)
        
    advisor = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Select Advisor",
                "class": "form-control"
            }
        ),required=False, queryset=Advisor.objects.all())