from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.8000 --> Local
    # myapp.com --> online
    path('', views.post_list, name='post_list'),

    # 127.0.0.8000/post/1 --> Local
    # myapp.com/post/1 --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]