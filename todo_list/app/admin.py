from django.contrib import admin
from .models import Student, Todo
from .models import Teacher

admin.site.register(Student)
admin.site.register(Todo)
admin.site.register(Teacher)
