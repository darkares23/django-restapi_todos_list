# Generated by Django 3.0.8 on 2020-08-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='lastName')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
