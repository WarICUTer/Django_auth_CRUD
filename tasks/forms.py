from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'descrip', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Write a Title'}),
            'descrip': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write a Description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center',})
        }