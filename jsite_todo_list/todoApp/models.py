from django.db import models

class Todo(models.Model):
    textTodo = models.fields.CharField(max_length=300)
    #textTodo = models.TextField()    
    
    def __str__(self):
        return self.textTodo




