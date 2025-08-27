from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name


class Subtask(BaseModel):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey(Task, on_delete=models.CASCADE)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.prog_name


class Category(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.name


class Priority(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")

    def __str__(self):
        return self.name


class Note(BaseModel):
    student = models.ForeignKey(Priority, on_delete=models.CASCADE)
    organization = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateField()

    status = models.CharField(max_length=50,choices=[("Pneding","Pending"),("In Progress","In Progress"),("Completed","Completed")],default="Pending")
