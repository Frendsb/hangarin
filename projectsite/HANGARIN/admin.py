from django.contrib import admin

from .models import Task, Subtask, Category, Priority, Note

admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Note)