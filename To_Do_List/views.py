from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def Home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    print(todo_items)
    return render(request, 'To_Do_List/index.html', {"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    # print(created_obj)
    # print(created_obj.id)
    return HttpResponseRedirect("http://127.0.0.1:8000/todo_app/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/todo_app/")