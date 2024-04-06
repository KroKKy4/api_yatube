from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
# router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
#                    basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/posts/<int:post_id>/comments/', CommentViewSet.as_view(),
         name='comment-list'),
    path('v1/posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view(),
         name='comment-detail'),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
