"""
Urls for rest api
"""


from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('todo_list/', views.todoList, name='todo_list'),
    path('todo_detail/<str:pk>/', views.todoDetail, name='todo_detail'),
    path('todo_update/<str:pk>/', views.todoUpdate, name='todo_update'),
    path('todo_delete/<str:pk>/', views.todoDelete, name='todo_delete'),
    path('todo_create/', views.todoCreate, name='todo_create'),
    path('todo/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
