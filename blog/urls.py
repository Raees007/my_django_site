from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


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

    # 127.0.0.8000/drafts --> Local
    # myapp.com/drafts --> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 127.0.0.8000/post/2/publish --> Local
    # myapp.com/post/2/publish --> online
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    # 127.0.0.8000/post/2/comment/ --> Local
    # myapp.com/post/2/comment/ --> online
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]