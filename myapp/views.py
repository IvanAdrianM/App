from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def index(request):
    titulo = "Bienvenido ProjectGO!!!"
    return render(request, "Index.html", {"titulo": titulo})


def about(request):
    return render(request, "about.html")


def project(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


def task(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        form = CreateNewTask()
        return render(request, "tasks/create_task.html", {"form": form})
    else:
        # Obtener los datos del formulario
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                project_id=form.cleaned_data["project"],
            )
            return redirect("/tasks/")
        else:
            # Si el formulario no es válido, vuelve a mostrar la página con los errores
            return render(request, "tasks/create_task.html", {"form": form})


def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", 
            {"form": CreateNewProject()}
        )
    else:
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return render(request, "projects/create_project.html", 
            {"form": CreateNewProject()
            })
        return redirect("/projects/")


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : tasks
    })


def eliminar_tarea(request, task_id):
    if request.method == 'POST':
        tarea = get_object_or_404(Task, id=task_id)
        tarea.delete()
        return JsonResponse({'mensaje': 'Tarea eliminada correctamente.'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def marcar_completada(request, task_id):
    if request.method == 'POST':
        tarea = get_object_or_404(Task, id=task_id)
        tarea.hecho = True
        tarea.save()
        return JsonResponse({'mensaje': 'Tarea marcada como completada.'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def eliminar_proyecto(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('/projects/')


def marcar_proyecto_hecho(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.hecho = True
    project.save()
    return redirect('/projects/')