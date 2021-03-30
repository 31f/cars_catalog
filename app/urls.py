from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.catalog import views

router = routers.DefaultRouter()
router.register(r'makes', views.MakeViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'submodels', views.SubmodelViewSet)
router.register(r'cars', views.CarViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
