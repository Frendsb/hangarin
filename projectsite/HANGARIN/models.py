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

    def __str__(self):
        return self.prog_name


class Category(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Priority(BaseModel):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Subtask, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"


class Note(BaseModel):
    student = models.ForeignKey(Priority, on_delete=models.CASCADE)
    organization = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateField()
