# Generated by Django 3.0.8 on 2020-08-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200801_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='done',
        ),
        migrations.RemoveField(
            model_name='person',
            name='title',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='name', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='name', max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
