# Generated by Django 4.1.7 on 2023-03-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
