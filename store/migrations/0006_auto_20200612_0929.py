# Generated by Django 3.0.7 on 2020-06-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200612_0756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopitem',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
