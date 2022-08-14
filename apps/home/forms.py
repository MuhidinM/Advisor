from django import forms
from django.forms import ModelForm
from .models import Student, Advisor


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
    program_choices = (
        ('pre engineering' , 'Pre Engineering'),
        ('pre science', 'Pre Science')
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ), required=False)
    program = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Program",
                "class": "form-control"
            }
        ),choices=program_choices, required=False)
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


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))
    school = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "School",
                "class": "form-control"
            }
        ))
    
    
    
class AssignForm(ModelForm):
    class Meta:
        model = Student
        fields = ('advisor', 'section')
        
    advisor = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Select Advisor",
                "class": "form-control"
            }
        ),required=False, queryset=Advisor.objects.all())
    
    section = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Section",
                "class": "form-control"
            }
        ), max_value=100, min_value=1, required=False)
    
class AssignIndividualForm(ModelForm):
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