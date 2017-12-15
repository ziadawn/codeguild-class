from django.db import models

# Create your models here.

from django.db import models

class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)            # this variable has to match the same one in views

    def __str__(self):              # this controls how things are displayed in the admin panel
        return self.todo_text