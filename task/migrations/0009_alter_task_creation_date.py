# Generated by Django 5.0 on 2023-12-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_alter_task_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
