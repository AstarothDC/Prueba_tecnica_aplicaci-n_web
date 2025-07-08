from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, index

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('inicio/', index, name='inicio'),
]