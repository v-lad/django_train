from django.urls import path, re_path
from .views import *

# app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name="post_list_url"), 
    path('post/create/', PostCreate.as_view(), name="post_create_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('post/<str:slug>/update', PostUpdate.as_view(), name="post_update_url"),
    path('post/<str:slug>/delete', PostDelete.as_view(), name="post_delete_url"),
    path('tags/', TagsList.as_view(), name="tags_list_url"),
    path('tags/create/', TagCreate.as_view(), name="tag_create_url"),
    path('tags/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name="tag_update_url"),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name="tag_delete_url")
]