from django.urls import path
from . import views


app_name = "api"

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.get_files, name='get_files'),
]

# handler404 = views.pageNotFound
