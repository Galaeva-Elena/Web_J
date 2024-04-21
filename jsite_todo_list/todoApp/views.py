from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from todoApp.models import Todo
from todoApp.forms import TodoForm


def index(request):
    context = {
        'title' : 'Задание 3 "Список дел"'
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h2>Главная</h2>")


def todoList(request):
   #return HttpResponse("<h2>Список дел</h2>")
    context = {
        'title' : 'Список задач/дел',
        'todoList' : Todo.objects.all()
    }
    return render(request, "todoList.html", context)


def addTodo(request):    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            
            return HttpResponseRedirect("todoList")        
        
    else:
        form = TodoForm()

    return render(request, 'addTodo.html', {'form': form})
    #return HttpResponse("<h2>Добавлени нового дела</h2>")
    
#2nd method    
""" def addTodo(request):
    if request.method == 'POST':
        textTodo = request.POST.get("textTodo", "Пустой запрос!")
        newtask = Todo.objects.create(textTodo=textTodo)
        print(newtask)
        return HttpResponseRedirect("todoList")
    else:   
        return render(request, "addTodo.html") """
       
   
def delTodo(request, todo_id):
    try:
        Todo.objects.get(id=todo_id).delete()
        return HttpResponseRedirect(reverse('todoList'))
    except Todo.DoesNotExist:
        return HttpResponse("Задача/дело не существует.")
    
    
def editTodo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)

        if request.method == 'POST':
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/todoApp/todoList")
        else:
            form = TodoForm(instance=todo)

        return render(request, 'editTodo.html', {'form': form})
    except Todo.DoesNotExist:
        return HttpResponse("Задача/дело не существует.")