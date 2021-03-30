from rest_framework import serializers

from app.catalog.models import Make, Model, Submodel, Car


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name', 'active']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name', 'active', 'make']


class SubmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submodel
        fields = ['id', 'name', 'active', 'model', 'make']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'active', 'mileage', 'price', 'submodel', 'model', 'make', 'body_type', 'transmission',
                  'fuel_type', 'exterior_color']
