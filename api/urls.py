from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (PostViewSet, CommentViewSet,
                    FollowViewSet, GroupViewSet)


app_name = 'api_posts'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = []

v1_urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/', include(router_v1.urls)),
    path('v1/follow/', FollowViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='follow'),
    path('v1/group/', GroupViewSet.as_view(
        {'get': 'list', 'post': 'create'},
    ), name='group'),
]

urlpatterns += v1_urlpatterns
