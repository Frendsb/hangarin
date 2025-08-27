from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    Task_name = models.CharField(max_length=150)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.Task_name

class Subtask(BaseModel):
    Subtask_name = models.CharField(max_length=150)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.Subtask_name

class Priority(BaseModel):
    priority = models.CharField(max_length=150)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.priority

class Category(BaseModel):
    category = models.CharField(max_length=150)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.category

class Note(BaseModel):
    note_name = models.CharField(max_length=150)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.note_name