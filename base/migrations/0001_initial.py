# Generated by Django 4.0.1 on 2022-01-23 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneContacts', models.CharField(max_length=200)),
                ('ownerEmail', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('idnumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OwnershipStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SingleProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('area', models.CharField(max_length=200)),
                ('starting_price', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.TextField(max_length=200)),
                ('propertyInfrastructure', models.TextField(max_length=300)),
                ('propertyAmenities', models.TextField(max_length=400)),
                ('siteVisitDays', models.CharField(max_length=10)),
                ('howToBuy', models.TextField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.owner')),
                ('propertyStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ownershipstatus')),
                ('propertyType', models.ManyToManyField(to='base.PropertyUsage')),
            ],
        ),
    ]