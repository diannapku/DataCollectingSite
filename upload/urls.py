from django.urls import path

from . import views


app_name = 'upload'
urlpatterns = [
    path('', views.home, name='home'),
    path('file', views.upload_file),
]
