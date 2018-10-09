from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.8000 --> Local
    path('', views.post_list, name='post_list')
]