from django.contrib import admin
from .models import Tutor, Discipline, Workplace


@admin.register(Tutor, Discipline, Workplace)
class AuthorAdmin(admin.ModelAdmin):
    pass
