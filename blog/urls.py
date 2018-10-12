from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.8000 --> Local
    # myapp.com --> online
    path('', views.post_list, name='post_list'),

    # 127.0.0.8000/post/1 --> Local
    # myapp.com/post/1 --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.8000/post/new --> Local
    # myapp.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),

    # 127.0.0.8000/post/2/edit --> Local
    # myapp.com/post/2/edit --> online
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]