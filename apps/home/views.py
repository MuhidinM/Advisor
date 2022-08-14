from apps.home.models import Advisor, Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from tablib import Dataset

from .forms import AdvisorForm, AssignForm, AssignIndividualForm, StudentForm
from .resources import StudentResource


@login_required(login_url="/login/")
def index(request):
    student = Student.objects.all()
    context = {'segment': 'dashboard', 'student': student}
    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def assignsection(request):
    form = AssignForm()
    if request.method == 'POST':
        form = AssignForm(request.POST)
        if form.is_valid():
            advisor = form.cleaned_data['advisor'].name
            section = form.cleaned_data['section']
            Student.objects.filter(section=section).update(advisor=advisor)
        context = {'segment': 'assign'}
        return redirect('dashboard')

    context = {'segment': 'assign', 'form': form}
    return render(request, 'home/assignsection.html', context)


@login_required(login_url="/login/")
def dashboard(request):
    student = Student.objects.all()
    context = {'segment': 'dashboard', 'student': student}
    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def student(request):
    student = Student.objects.all()
    context = {'segment': 'student', 'items': student}
    return render(request, 'home/students.html', context)


@login_required(login_url="/login/")
def advisor(request):
    advisors = Advisor.objects.all()
    context = {'segment': 'advisor', 'items': advisors}
    return render(request, 'home/advisors.html', context)


@login_required(login_url="/login/")
def assign(request, pk):
    student = Student.objects.get(id=pk)
    form = AssignIndividualForm(instance=student)
    if request.method == 'POST':
        form = AssignIndividualForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'segment': 'assign', 'form': form}
    return render(request, 'home/assign.html', context)


@login_required(login_url="/login/")
def addstu(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')

    context = {'segment': 'addstu', 'form': form}
    return render(request, 'home/addstu.html', context)


@login_required(login_url="/login/")
def updstu(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')

    context = {'form': form}
    return render(request, 'home/addstu.html', context)


@login_required(login_url="/login/")
def addadv(request):
    msg = None
    success = False
    form = AdvisorForm()

    if request.method == 'POST':
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advisor')
        else:
            msg = 'Form is not valid'

    context = {'segment': 'addstu', 'form': form}
    return render(request, 'home/addadv.html', context)


@login_required(login_url="/login/")
def updadv(request, pk):
    msg = None
    success = False
    student = Advisor.objects.get(id=pk)
    form = AdvisorForm(instance=student)
    if request.method == 'POST':
        form = AdvisorForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('advisor')
        else:
            msg = 'Form is not valid'

    context = {'form': form}
    return render(request, 'home/addadv.html', context)


@login_required(login_url="/login/")
def delete_stu(request, pk):
    item = Student.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('student')
    context = {'item': item}
    return render(request, 'home/delete_stu.html', context)


@login_required(login_url="/login/")
def delete_adv(request, pk):
    item = Advisor.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('advisor')
    context = {'item': item}
    return render(request, 'home/delete_adv.html', context)


@login_required(login_url="/login/")
def student_list(request):
    context = {}
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'home/exportstudent.htm')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
    return render(request, 'home/exportstudent.html', context)
