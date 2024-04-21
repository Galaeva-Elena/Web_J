from django import forms
from todoApp.models import Todo

class TodoForm(forms.ModelForm):
   class Meta:
     model = Todo
     fields = '__all__'
     
#class TodoForm(forms.Form):
    #todo_text = forms.CharField(label="Задача/дело:", max_length=300)