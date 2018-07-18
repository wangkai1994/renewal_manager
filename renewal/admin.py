from django.contrib import admin

# Register your models here.
from renewal.models import Project

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, AuthorAdmin)
