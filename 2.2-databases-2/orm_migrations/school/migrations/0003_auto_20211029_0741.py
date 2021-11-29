# Generated by Django 3.2.7 on 2021-10-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20211029_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='student', to='school.Teacher'),
        ),
    ]
