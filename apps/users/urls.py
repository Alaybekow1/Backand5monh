from django.urls import path

from apps.users.views import RegisterView, LoginView ,ProfileView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename='users')
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="LIbrary 28-1B",
        default_version='v1',
        description='LIBRARY 28-1B',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email=''),
        e
)
urlpatterns = [
    path("register", RegisterView.as_view(),name='register'),
    path('login', LoginView.as_view(),name='login'),
    path("profile", ProfileView.as_view(),name='profile')

path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

url
