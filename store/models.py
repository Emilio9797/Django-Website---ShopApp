from django.db import models
from django.urls import reverse
from decimal import Decimal


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    picture = models.ImageField(blank=False, default='index.jpeg')

    def get_absolute_url(self):
        return reverse('store:category_view', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ActiveItemManager(models.Manager):
    def get_queryset(self):
        return super(ActiveItemManager, self).get_queryset().filter(active=True)


class ShopItem(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_expires = models.DateTimeField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    active = models.BooleanField(default=True)

    picture = models.ImageField(blank=False, default='index.jpeg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ShopItems')

    objects = models.Manager()
    active_items = ActiveItemManager()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:shop-detail', args=[self.id, self.slug])


class GalleryItem(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    primary_picture = models.ImageField(blank=False, default='index.jpeg')
    slug = models.SlugField(max_length=200, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=1000, default='**Awesome** picture, and *model*.')

    objects = models.Manager()
    active_items = ActiveItemManager()

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:gallery-detail', args=[self.id, self.slug])


class GalleryPicture(models.Model):
    gallery_item = models.ForeignKey(GalleryItem, on_delete=models.CASCADE)
    picture = models.ImageField(blank=False, default='index.jpeg')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_item.name + ' #' + str(self.id)

class DeliveryOption(models.Model):
    picture = models.ImageField(blank=False, default='index.jpeg')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_price(self):
        return Decimal(self.price)


    class Meta:
        ordering = ('price',)

