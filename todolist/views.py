from django.shortcuts import render , redirect
from . models import Todolist #import todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    todo_items = Todolist.objects.order_by('id') # create variable to retrive data from DB and order them by id
    context = {'todo_items' : todo_items} # it's a dictionary and returns todo_items variable
    return render(request, 'todolist\index.html', context)#this will pass the information to the template.

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text']) 
        new_todo.save()
    

    return redirect('index')


def completedTodo(request, todo_id)  :  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')


