from django.db import models

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length=45)  #here we are define the fields for the model(in our case text). CharField is a data type, and the lenght of characters
    completed = models.BooleanField(default = False)  #Boolean field is a True or Faulse syntax. Default the todolist should never be completed
    
    def __str__(self) : # return a text as a representation of Todo
        return self.text #text is the one from above
    