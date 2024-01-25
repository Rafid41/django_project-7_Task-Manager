# Generated by Django 4.2.9 on 2024-01-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=10),
        ),
    ]