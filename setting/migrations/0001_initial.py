# Generated by Django 3.2.8 on 2023-01-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising_Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='Advertising')),
                ('img2', models.ImageField(upload_to='Advertising')),
                ('img3', models.ImageField(upload_to='Advertising')),
            ],
        ),
    ]