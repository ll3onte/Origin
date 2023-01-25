from django.contrib import admin
from . models import Todolist  # "." is used to let the program know that you are importing from the same directory

# Register your models here.

admin.site.register(Todolist) #this is how you register the model