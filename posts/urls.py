from django.urls import path,re_path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)

urlpatterns=[

   # path('',views.index,name='posts-index'),
   path('',PostListView.as_view(),name='posts-index'),
   # re_path('details/(?P<id>\d+)/',views.details,name='details'),
   path('details/<int:pk>/',PostDetailView.as_view(),name='details'),
   path('new/',PostCreateView.as_view(),name='post-create'),
   path('details/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('details/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),  
 
]



