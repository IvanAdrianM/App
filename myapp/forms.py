from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Título de tarea", 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    description = forms.CharField(
        label="Descripción de la tarea", 
        widget=forms.Textarea(attrs={'class': 'input'})
    )
    project = forms.ChoiceField(
        label="Proyecto", 
        choices=[], 
        widget=forms.Select(attrs={'class': 'input'})
    )

    def __init__(self, *args, **kwargs):
        super(CreateNewTask, self).__init__(*args, **kwargs)
        # Cargar proyectos dinámicamente al inicializar el formulario
        self.fields['project'].choices = [(project.id, project.name) for project in Project.objects.all()]


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))