# Generated by Django 3.0.7 on 2020-07-13 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_galleryitem_gallerypicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
        migrations.AlterField(
            model_name='gallerypicture',
            name='gallery_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.GalleryItem'),
        ),
    ]
