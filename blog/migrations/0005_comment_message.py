# Generated by Django 3.2.8 on 2023-01-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
