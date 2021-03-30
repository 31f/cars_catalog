**Cars Catalog Application**

Python 3.8 / Django 3.1.7

---
**Run**:

`$ pip install virtualenv`

`$ virtualenv myvenv`

`$ source myvenv/bin/activate`

`$ pip install -r requirements.txt`

`$ python manage.py runserver`

At browser go to http://127.0.0.1:8000/

---

**API endpoints**:

`api/makes` - car makes list

`api/models` - car models list

`api/submodels` - car submodels list

`api/cars` - cars list. 

Filters: `price_more`, `price_less`, `name`, `mileage_more`, `mileage_less` 

`api/cars/{car_id}` - selected car details
