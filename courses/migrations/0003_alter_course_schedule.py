# Generated by Django 4.2.3 on 2023-08-25 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 21, 57, 30, 463284)),
        ),
    ]