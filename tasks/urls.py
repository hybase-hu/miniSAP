from django.urls import path

from tasks.views import all_task_views, task_view, task_modify, my_tasks_list, add_new_task

app_name = "tasks"
urlpatterns = [
    path('', all_task_views),
    path('task/<int:id>/', task_view,name="task_view"),
    path('task/<int:id>/modify/', task_modify,name="task_modify"),
    path('task/my/', my_tasks_list,name="my_tasks_list"),
    path('task/add/', add_new_task,name="add_new_task"),
]
