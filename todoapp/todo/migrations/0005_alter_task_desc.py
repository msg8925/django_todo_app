# Generated by Django 4.1.3 on 2022-11-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.TextField(default=False),
        ),
    ]
