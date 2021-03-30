from django.contrib import admin

from app.catalog.models import Car, Model, Submodel, Make


@admin.register(Submodel)
class SubmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'year', 'mileage', 'price', 'created_at', 'updated_at')
