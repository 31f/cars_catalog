from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.catalog.models import Make, Model, Submodel, Car


class APITestCase(TestCase):
    client_class = APIClient


class MakeAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.make = Make.objects.create(id='acura', name='Acura', active=True)
        self.model = Model.objects.create(id='1051', name='MDX', active=True, make=self.make)
        self.submodel = Submodel.objects.create(id='589', name='MDX2000', active=True, model=self.model)
        self.car = Car.objects.create(active=True, year=2009, mileage=150000, price=52000, submodel=self.submodel,
                                      body_type='SUV', transmission='Automatic', fuel_type='Petrol',
                                      exterior_color='White')

    def test_makes(self):
        resp = self.client.get('/api/makes/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        make = resp.data[0]
        self.assertEqual(make['id'], self.make.id)
        self.assertEqual(make['name'], self.make.name)
        self.assertEqual(make['active'], self.make.active)

    def test_models(self):
        resp = self.client.get('/api/models/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        model = resp.data[0]
        self.assertEqual(model['id'], self.model.id)
        self.assertEqual(model['name'], self.model.name)
        self.assertEqual(model['active'], self.model.active)
        self.assertEqual(model['make'], self.model.make.name)

    def test_submodels(self):
        resp = self.client.get('/api/submodels/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        submodel = resp.data[0]
        self.assertEqual(submodel['id'], self.submodel.id)
        self.assertEqual(submodel['name'], self.submodel.name)
        self.assertEqual(submodel['active'], self.submodel.active)
        self.assertEqual(submodel['model'], self.model.name)
        self.assertEqual(submodel['make'], self.model.make.name)

    def test_cars(self):
        resp = self.client.get('/api/cars/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        car = resp.data[0]
        self.assertEqual(car['id'], str(self.car.id))
        self.assertEqual(car['year'], self.car.year)
        self.assertEqual(car['mileage'], self.car.mileage)
        self.assertEqual(car['active'], self.car.active)
        self.assertEqual(car['model'], self.car.model.name)
        self.assertEqual(car['make'], self.car.make.name)
        self.assertEqual(car['submodel'], self.car.submodel.name)
        self.assertEqual(car['price'], self.car.price)
        self.assertEqual(car['body_type'], self.car.body_type)
        self.assertEqual(car['transmission'], self.car.transmission)
        self.assertEqual(car['fuel_type'], self.car.fuel_type)
        self.assertEqual(car['exterior_color'], self.car.exterior_color)
