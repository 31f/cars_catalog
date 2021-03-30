import django_filters
from django_filters.rest_framework import FilterSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.catalog.models import Make, Model, Submodel, Car
from app.catalog.serializers import MakeSerializer, ModelSerializer, SubmodelSerializer, CarSerializer


class MakeViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer


class ModelViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class SubmodelViewSet(mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Submodel.objects.all()
    serializer_class = SubmodelSerializer


class CarsFilter(FilterSet):
    price_more = django_filters.DateFilter(method='price_more_filter')
    price_lower = django_filters.DateFilter(method='price_lower_filter')

    mileage_more = django_filters.DateFilter(method='mileage_more_filter')
    mileage_lower = django_filters.DateFilter(method='mileage_lower_filter')

    name = django_filters.DateFilter(method='name_filter')

    class Meta:
        model = Car
        fields = ['price_more', 'price_lower', 'name', 'mileage_more', 'mileage_lower']

    def price_more_filter(self, queryset, name, value):
        return queryset.exclude(price__gte=value)

    def price_lower_filter(self, queryset, name, value):
        return queryset.exclude(price__lte=value)

    def mileage_more_filter(self, queryset, name, value):
        return queryset.exclude(mileage__gte=value)

    def mileage_lower_filter(self, queryset, name, value):
        return queryset.exclude(mileage__lte=value)

    def name_filter(self, queryset, name, value):
        return queryset.filter(submodel__model_name__icontains=value)


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarsFilter
    ordering = ['-updated_at']
