from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from axes.decorators import axes_dispatch

from apps.security import views

urlpatterns = [
    path('', views.UserCreateApiView.as_view(), name='users'),
    path('<uuid:id>/', views.UserUpdateDestroyApiView.as_view(), name='users'),
    path('token/', axes_dispatch(TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('token/refresh/', axes_dispatch(TokenRefreshView.as_view()), name='token_refresh'),
]
