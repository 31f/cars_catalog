"""
Methods for safe data import from source csv to our database schema.

Run one by one:
import_makes()
import_models()
import_submodels()
import_cars()
"""
import dateutil.parser
from .models import Make, Model, Submodel, Car

makes_csv = ''''''

models_csv = ''''''


submodels_csv = ''''''


cars_csv = ''''''


def import_makes():
    makes_list = makes_csv.split('\n')
    imported = 0
    print(f'Makes. Lines of data: {len(makes_list)}')
    for m in makes_list:
        make = m.split('\t')
        if len(make) > 1:
            active = make[2] == 't'
            created = dateutil.parser.parse(make[3])
            updated = dateutil.parser.parse(make[4])
            make, is_created = Make.objects.get_or_create(
                id=make[0],
                defaults={'name': make[1],
                          'active': active,
                          'created_at': created,
                          'updated_at': updated,
                          })
            if is_created:
                imported += 1
    print(f'Imported: {imported}')


def import_models():
    models_list = models_csv.split('\n')
    imported = 0
    print(f'Models. Lines of data: {len(models_list)}')
    for m in models_list:
        model = m.split('\t')
        if len(model) > 1:
            active = model[2] == 't'
            created = dateutil.parser.parse(model[4])
            updated = dateutil.parser.parse(model[5])

            if not Make.objects.filter(id=model[3]).exists():
                print(f'No make - {model[3]}')

            model, is_created = Model.objects.get_or_create(
                id=model[0],
                defaults={'name': model[1],
                          'active': active,
                          'make_id': model[3],
                          'created_at': created,
                          'updated_at': updated,
                          })
            if is_created:
                imported += 1
    print(f'Imported: {imported}')


def import_submodels():
    submodels_list = submodels_csv.split('\n')
    imported = 0
    print(f'Submodels. Lines of data: {len(submodels_list)}')
    for m in submodels_list:
        submodel = m.split('\t')
        if len(submodel) > 1:
            active = submodel[2] == 't'
            created = dateutil.parser.parse(submodel[4])
            updated = dateutil.parser.parse(submodel[5])

            if not Model.objects.filter(id=submodel[3]).exists():
                print(f'No model - {submodel[3]}')

            submodel, is_created = Submodel.objects.get_or_create(
                id=submodel[0],
                defaults={'name': submodel[1],
                          'active': active,
                          'model_id': submodel[3],
                          'created_at': created,
                          'updated_at': updated,
                          })
            if is_created:
                imported += 1
    print(f'Imported: {imported}')


def import_cars():
    cars_list = cars_csv.split('\n')
    imported = 0
    print(f'Cars. Lines of data: {len(cars_list)}')
    for m in cars_list:
        car = m.split('\t')
        if len(car) > 1:
            active = car[1] == 't'
            year = int(car[2])
            mileage = int(car[3]) if car[3] != '' else 0
            price = int(car[4]) if car[4] != '' else 0

            if not Make.objects.filter(id=car[5]).exists():
                print(f'No make - {car[5]}')

            if not Model.objects.filter(id=car[6]).exists():
                print(f'No model - {car[6]}')

            if not Submodel.objects.filter(id=car[7]).exists():
                print(f'No submodel - {car[7]}')

            created = dateutil.parser.parse(car[12])
            updated = dateutil.parser.parse(car[13])

            car, is_created = Car.objects.get_or_create(
                id=car[0],
                defaults={'id': car[0],
                          'active': active,
                          'year': year,
                          'mileage': mileage,
                          'price': price,
                          'submodel_id': car[7],
                          'body_type': car[8],
                          'transmission': car[9],
                          'fuel_type': car[10],
                          'exterior_color': car[11],
                          'created_at': created,
                          'updated_at': updated,
                          })
            if is_created:
                imported += 1
    print(f'Imported: {imported}')
