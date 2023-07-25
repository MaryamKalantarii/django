# Generated by Django 4.2.3 on 2023-07-25 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_statuse_course_status_alter_course_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.JPG', upload_to='course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 10, 40, 50, 355610)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(default='teacher.png', upload_to='trainer'),
        ),
    ]