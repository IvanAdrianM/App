from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.index),
    path('about/' ,views.about),
    path('projects/' ,views.project),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('tasks/' ,views.task),
    path('index/' ,views.index),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/' ,views.create_project),
   path('eliminar-tarea/<int:task_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('marcar-completada/<int:task_id>/', views.marcar_completada, name='marcar_completada'),
    path('eliminar-proyecto/<int:project_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('marcar-proyecto-hecho/<int:project_id>/', views.marcar_proyecto_hecho, name='marcar_proyecto_hecho'),
]