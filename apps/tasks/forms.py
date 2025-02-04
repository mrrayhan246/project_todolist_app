from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completed']

    due_date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    priority = forms.ChoiceField(
        choices=Task.PRIORITY_CHOICES,
        widget=forms.RadioSelect
    )
