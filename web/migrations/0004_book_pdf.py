# Generated by Django 3.2.12 on 2023-05-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]
