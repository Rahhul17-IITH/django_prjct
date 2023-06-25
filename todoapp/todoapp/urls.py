from django.urls import path
from todos import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.create_todo, name='create_todo'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('todos/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),

]
