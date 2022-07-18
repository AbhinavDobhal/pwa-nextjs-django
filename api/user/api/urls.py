from django.urls import path
from user.api.views import(
    registration_view,
    ObtainAuthTokenView,
    test_view,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('test/', test_view),
    path('register/', registration_view),
    path('login/', ObtainAuthTokenView.as_view()),
]
