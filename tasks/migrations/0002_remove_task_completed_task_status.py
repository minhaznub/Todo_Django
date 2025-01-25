# Generated by Django 5.1.5 on 2025-01-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('inprogress', 'In Progress'), ('done', 'Done')], default='new', max_length=20),
        ),
    ]
