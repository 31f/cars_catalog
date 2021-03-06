# Generated by Django 3.1.7 on 2021-03-30 20:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('active', models.BooleanField()),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('active', models.BooleanField()),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='models', to='catalog.make')),
            ],
        ),
        migrations.CreateModel(
            name='Submodel',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('active', models.BooleanField()),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submodels', to='catalog.model')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('year', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900)], verbose_name='Year')),
                ('mileage', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('body_type', models.CharField(blank=True, max_length=300)),
                ('transmission', models.CharField(blank=True, max_length=300)),
                ('fuel_type', models.CharField(blank=True, max_length=300)),
                ('exterior_color', models.CharField(blank=True, max_length=300)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('submodel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.submodel')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
    ]
