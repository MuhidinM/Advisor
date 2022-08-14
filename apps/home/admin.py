# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'studentid', 'section', 'program')