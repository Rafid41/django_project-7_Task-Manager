# Generated by Django 4.2.9 on 2024-01-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
        migrations.AddField(
            model_name='task',
            name='images',
            field=models.ManyToManyField(blank=True, to='tasks.image'),
        ),
    ]
