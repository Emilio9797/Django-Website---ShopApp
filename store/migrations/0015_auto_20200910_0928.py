# Generated by Django 3.0.7 on 2020-09-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_galleryitem_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryitem',
            options={'ordering': ('date_added',)},
        ),
    ]
