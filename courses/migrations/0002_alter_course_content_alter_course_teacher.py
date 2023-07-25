# Generated by Django 4.2.3 on 2023-07-24 18:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(default=datetime.datetime(2023, 7, 24, 23, 1, 14, 152995)),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.trainer'),
        ),
    ]