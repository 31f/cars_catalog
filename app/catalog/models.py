import uuid

from django.core.validators import MinValueValidator
from django.db import models
from model_utils.fields import AutoLastModifiedField, AutoCreatedField
from model_utils.models import TimeStampedModel


class Make(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    active = models.BooleanField()
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()


class Model(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    active = models.BooleanField()
    make = models.ForeignKey(Make, on_delete=models.PROTECT, related_name='models')
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()


class Submodel(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    active = models.BooleanField()
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name='submodels')
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()

    @property
    def make(self):
        return self.model.make


class Car(TimeStampedModel):
    id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, editable=False, primary_key=True)
    active = models.BooleanField()
    year = models.SmallIntegerField(verbose_name='Year',
                                    validators=[MinValueValidator(1900)],
                                    blank=True, null=True)
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    submodel = models.ForeignKey(Submodel, on_delete=models.PROTECT)
    body_type = models.CharField(max_length=300, blank=True)
    transmission = models.CharField(max_length=300, blank=True)
    fuel_type = models.CharField(max_length=300, blank=True)
    exterior_color = models.CharField(max_length=300, blank=True)
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    @property
    def model(self):
        return self.submodel.model

    @property
    def make(self):
        return self.submodel.model.make
