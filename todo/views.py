from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.

# def home_view(request):
#     return HttpResponse('<h1>Todo Application</h1>')

def home_view(request):
    todos = Todo.objects.filter(is_active=True)
    context = dict(
        todos = todos,
    )
    return render(request, 'todo/todo_list.html', context)