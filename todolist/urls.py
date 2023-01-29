from django.urls import path
from . import views # views from the same directory with todo list

urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'), 
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]
