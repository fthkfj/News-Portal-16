from django.urls import path
from .views import PostList, PostDetail, Search, PostCreate, PostUpdate, PostDelete, Subscribes
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', Search.as_view()),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscribe/', cache_page(60*5)(Subscribes.as_view()), name='subscribe'),
]
