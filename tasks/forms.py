from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):

    

    class Meta:
        model = Task
        fields = ['assigned_user', 'task_name', 'task_description', 'deadline']


        labels = {
            'assigned_user': 'Assigned user',
            'task_name': 'Task Name',
            'task_description': 'Task Description',
            'deadline': 'Deadline Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['task_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['task_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['assigned_user'].widget.attrs.update({'class': 'form-control'})

        self.fields['deadline'].widget = forms.DateInput(attrs={'type':'datetime-local','class':'form-control'})
