from django.contrib import admin
from .models import SubjectsModel, StudentModel

# Register your models here.


admin.site.register(SubjectsModel)
admin.site.register(StudentModel)