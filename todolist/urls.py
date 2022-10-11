from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete, name='delete'),
    path('json/', todolist_json, name='todolist_json'),
    path('add/', add_task, name='add_task')
]