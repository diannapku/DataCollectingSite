from django.urls import path

from . import views


app_name = 'download'
urlpatterns = [
    path('', views.show_list, name='project_list'),
    path('detail/<project_name>', views.show_detail),

]
