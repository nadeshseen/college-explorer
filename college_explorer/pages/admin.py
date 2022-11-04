from django.contrib import admin

from .models import TeacherMany, ResearchInterests

# Register your models here.

admin.site.register(TeacherMany)
admin.site.register(ResearchInterests)