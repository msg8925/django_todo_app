# Generated by Django 4.1.3 on 2022-11-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.TextField(default=None, max_length=256),
        ),
    ]
