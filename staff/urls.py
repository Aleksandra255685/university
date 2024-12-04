from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/<int:person_id>/', views.staff_detail, name='staff_detail'),
    path('disciplines/<slug:discipline_slug>/', views.discipline_persons,
         name='discipline_persons'),
    path('tasks/<slug:task_slug>/', views.task_persons,
         name='task_persons'),
]
