from rest_framework import viewsets

from menu.models import FoodCategory
from api.serializers import FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
