from django.urls import path
from .views import RegisterUserView, LoginUserView,RefreshTokenView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='manual_token_refresh'),

]
