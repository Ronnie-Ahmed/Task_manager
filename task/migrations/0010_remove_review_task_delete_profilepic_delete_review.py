# Generated by Django 5.0 on 2023-12-26 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_alter_task_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='task',
        ),
        migrations.DeleteModel(
            name='ProfilePic',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
