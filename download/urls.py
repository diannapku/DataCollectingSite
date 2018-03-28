from django.urls import path

from . import views


app_name = 'download'
urlpatterns = [
    path('', views.show_list, name='project_list'),
    path('search', views.search, name='search'),
    path('<project_name>', views.show_detail),
    path('<project_name>/<type>', views.show_more_detail, name='detail'),
    path('file/<project_name>', views.download, name='file'),

]
