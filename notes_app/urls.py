from django.urls import path
from . import views

urlpatterns =[
    path('', views.myNotesList, name='notes-list'),
    path('add-note/', views.addNote, name='add-note'),
    path('edit-note/<str:pk>/', views.editNote, name='edit-note'),
    path('view-note/<str:pk>/', views.viewNote, name='view-note'),
    path('delete-note/<str:pk>/', views.deleteNote, name='delete-note'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),
]