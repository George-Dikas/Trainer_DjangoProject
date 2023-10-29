from django.contrib import admin
from .models import Subject, Trainer


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    list_per_page = 10


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'subject', 'phone']
    search_fields = ['lastname', 'firstname', 'phone', 'subject__name']
    list_per_page = 10
    