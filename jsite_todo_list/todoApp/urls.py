from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="home"),
   path('todoList', views.todoList, name="todoList"),
   path('addTodo', views.addTodo, name="addTodo"),
   path('delTodo/<int:todo_id>/', views.delTodo, name="delTodo"),
   path('editTodo/<int:todo_id>/edit/', views.editTodo, name="editTodo"),
]  
