from rest_framework import serializers

from app.catalog.models import Make, Model, Submodel, Car


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id',
                  'name',
                  'active'
                  ]


class ModelSerializer(serializers.ModelSerializer):
    make = serializers.CharField(source='make.name')

    class Meta:
        model = Model
        fields = ['id',
                  'name',
                  'active',
                  'make'
                  ]


class SubmodelSerializer(serializers.ModelSerializer):
    model = serializers.CharField(source='model.name')
    make = serializers.CharField(source='make.name')

    class Meta:
        model = Submodel
        fields = ['id',
                  'name',
                  'active',
                  'model',
                  'make'
                  ]


class CarSerializer(serializers.ModelSerializer):
    model = serializers.CharField(source='model.name')
    make = serializers.CharField(source='make.name')
    submodel = serializers.CharField(source='submodel.name')

    class Meta:
        model = Car
        fields = ['id',
                  'active',
                  'year',
                  'mileage',
                  'price',
                  'submodel',
                  'model',
                  'make',
                  'body_type',
                  'transmission',
                  'fuel_type',
                  'exterior_color'
                  ]
