from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/<int:person_id>/', views.staff_detail, name='staff_detail'),
    path('disciplines/<slug:discipline_slug>/', views.discipline_tutor,
         name='discipline_tutor'),
    path('persons/create/', views.create_person, name='create_person'),
    path('persons/<int:person_id>/edit/', views.edit_person, name='edit_person'),
    path('persons/<int:person_id>/delete/', views.delete_person, name='delete_person'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
