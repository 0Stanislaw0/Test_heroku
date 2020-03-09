# Generated by Django 3.0.2 on 2020-03-09 14:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameru', models.CharField(max_length=150, verbose_name='Русское название')),
                ('nameen', models.CharField(max_length=150, verbose_name='Английское название')),
                ('year_of_creation', models.PositiveIntegerField(verbose_name='Год создания')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Reservations_cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата аренды')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата возвращения')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Cars')),
            ],
            options={
                'verbose_name': 'Аренда машины',
                'verbose_name_plural': 'Аренда машин',
            },
        ),
    ]
