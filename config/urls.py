from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from .views import MyTokenObtainPairCustomView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairCustomView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
