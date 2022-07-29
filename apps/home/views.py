# from cgitb import html
# from datetime import datetime
# import tempfile
# from unittest import result
# from urllib import response
from io import BytesIO

# from xhtml2pdf import pisa
from apps.home.models import Advisor, Student
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.template.loader import get_template
from django.urls import reverse
# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
# from weasyprint import HTML
# from io import BytesIO
from django.views import View
from xhtml2pdf import pisa

from .forms import AdvisorForm, StudentForm, AssignForm
from django.core.paginator import Paginator, EmptyPage

# import os



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    student = Student.objects.all()
    p = Paginator(student, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'segment': 'dashboard', 'student':page, 'p': p}
    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def student(request):
    student = Student.objects.all()
    p = Paginator(student, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'segment': 'student', 'items': page, 'p': p}
    return render(request, 'home/students.html', context)


@login_required(login_url="/login/")
def advisor(request):
    advisors = Advisor.objects.all()
    p = Paginator(advisors, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'segment': 'advisor', 'items': page, 'p': p}
    return render(request, 'home/advisors.html', context)


@login_required(login_url="/login/")
def assign(request, pk):
    msg = None
    success = False
    student = Student.objects.get(id=pk)
    form = AssignForm(instance=student)
    if request.method == 'POST':
        form = AssignForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            msg = 'Form is not valid'
    context = {'segment': 'assign', 'form': form}
    return render(request, 'home/assign.html', context)


@login_required(login_url="/login/")
def addstu(request):
    msg = None
    success = False
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            msg = 'Form is not valid'

    context = {'segment': 'addstu', 'form': form}
    return render(request, 'home/addstu.html', context)


@login_required(login_url="/login/")
def updstu(request, pk):
    msg = None
    success = False
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            msg = 'Form is not valid'

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
def student_list(request, *args, **kwargs):
    items = Student.objects.all()
    data = {'items': items}
    pdf = render_to_pdf('home/exportstudent.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url="/login/")
def advisor_list(request, *args, **kwargs):
    items = Advisor.objects.all()
    data = {'items': items}
    pdf = render_to_pdf('home/exportadvisors.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
   
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
