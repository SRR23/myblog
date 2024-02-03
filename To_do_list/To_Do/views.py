from django.shortcuts import render,redirect
from To_Do.forms import TaskModelForm
from To_Do.models import TaskModel
# Create your views here.

def home(request):
    return render(request, 'Home.html')

def Add_Tasks(request):
    if request.method == 'POST':
        To_Do = TaskModelForm(request.POST)
        if To_Do.is_valid():
            To_Do.save()
            return redirect('showtasks')
    else:
        To_Do = TaskModelForm()
    
    return render(request,'Add_Tasks.html', {'form' : To_Do})

def Show_Tasks(request):
    To_Do = TaskModel.objects.filter(is_completed=False)
    return render(request, 'Show_Tasks.html', {'data':To_Do})

def Complete_Task(request):
    To_Do = TaskModel.objects.filter(is_completed=True)
    return render(request, 'Complete_Tasks.html', {'data': To_Do})

def Edit_Task(request, id):
    To_Do = TaskModel.objects.get(pk = id)
    form = TaskModelForm(instance = To_Do)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance = To_Do)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
    return render(request,'Add_Tasks.html', {'form' : form})

def Delete_Task(request, id):
    To_Do = TaskModel.objects.get(pk = id).delete()
    return redirect('showtasks')

def Complete(request, id):
    To_Do = TaskModel.objects.get(pk = id)
    To_Do.is_completed = True
    To_Do.save()
    return redirect('completetasks')
