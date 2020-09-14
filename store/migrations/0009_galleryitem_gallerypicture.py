# Generated by Django 3.0.7 on 2020-07-11 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200711_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GalleryItems', to='store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='index.jpeg', upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('gallery_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='store.GalleryItem')),
            ],
        ),
    ]
