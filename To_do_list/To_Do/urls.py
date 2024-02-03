from django.urls import path
from To_Do.views import home, Add_Tasks, Show_Tasks, Edit_Task, Delete_Task, Complete_Task, Complete
urlpatterns = [
    path('', home),
    path('add_new_task/', Add_Tasks, name = 'addtasks'),
    path('show_all_task/', Show_Tasks, name = 'showtasks'),
    path('complete_all_task/', Complete_Task, name = 'completetasks'),
    path('edit_task/<str:id>', Edit_Task, name = 'edittasks'),
    path('delete_task/<str:id>', Delete_Task, name = 'deletetasks'),
    path('task_completed/<str:id>', Complete, name = 'taskcompleted'),
]