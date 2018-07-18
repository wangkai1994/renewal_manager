# from django.contrib import admin
from .models import Project
import xadmin


class ProjectAdmin(object):
    list_display = ('name', 'description', 'last_pay_at','next_pay_at','remarks')


xadmin.site.register(Project, ProjectAdmin)
