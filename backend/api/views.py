from django.db.models import Prefetch, Count, Q
from rest_framework import viewsets, mixins

from menu.models import FoodCategory, Food
from api.serializers import FoodCategorySerializer


class MenuViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''Представление для списка категорий с едой.'''

    serializer_class = FoodCategorySerializer

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
