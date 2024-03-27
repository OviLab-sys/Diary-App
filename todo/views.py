from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib import messages


def todo_list(request):
    activity_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'activity added successfully')
            return redirect('todo')
    form = TodoForm()
    return render(request,'todo/todo.html',{'form':form,
                                            'activity_list':activity_list,
                                            'title':"TODO LIST"})

def remove_activity(request,activity_id):
    activity = Todo.objects.get(id=activity_id)
    activity.delete()
    messages.info(request,'activity deleted successfully')
    return redirect('todo_list')