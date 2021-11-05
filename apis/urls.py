from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('add-note/', views.addNote, name='add-note'),
    path('edit-note/<str:pk>/', views.editNote, name='edit-note'),
    path('delete-note/<str:pk>/', views.deleteNote, name='delete-note'),
    path('delete-user/', views.deleteUser, name='delete-user'),
    path('note/<str:pk>/', views.viewNote, name='view-note'),
]