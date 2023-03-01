from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.security import views

urlpatterns = [
    path('', views.UserCreateApiView.as_view(), name='users'),
    path('<uuid:id>/', views.UserUpdateDestroyApiView.as_view(), name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
