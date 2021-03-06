# Generated by Django 3.2.6 on 2021-08-12 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250, unique=True)),
                ('start_year', models.IntegerField()),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='volkswagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('launching_year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.car')),
            ],
        ),
    ]
