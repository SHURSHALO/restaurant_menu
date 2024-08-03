from django.db.models import Prefetch, Count, Q
from rest_framework import viewsets

from menu.models import FoodCategory, Food
from api.serializers import FoodCategorySerializer


class FoodViewSet(viewsets.ModelViewSet):
    '''Представление для работы с категориями еды.'''

    serializer_class = FoodCategorySerializer
    http_method_names = ['get']

    def get_queryset(self):
        '''
        Возвращает queryset для получения категорий еды,
        которые содержат хотя бы одно опубликованное блюдо.
        '''

        queryset = FoodCategory.objects.annotate(
            published_food_count=Count('food', filter=Q(food__is_publish=True))
        ).filter(published_food_count__gt=0)

        queryset = queryset.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )

        return queryset
