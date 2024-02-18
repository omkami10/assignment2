from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views
from api.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
settings.STATIC_ROOT}), #serve static files when deployed
    path('api-auth/', include('rest_framework.urls')),  # Allow login/logout for non-admin from local server page
    path('api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.movie_list),
    path('api/movies/', views.movie_list),
    path('api/movies/<int:pk>/', views.getMovie),  # Added trailing slash
    path('register/', RegisterView.as_view(), name='auth_register'),
]
