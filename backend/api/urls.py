from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import MenuViewSet


router_v1 = DefaultRouter()

router_v1.register(r'foods', MenuViewSet, basename='foods'),

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
