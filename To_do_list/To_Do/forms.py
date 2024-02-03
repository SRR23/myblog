from django import forms
from To_Do.models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitel', 'taskDescription']