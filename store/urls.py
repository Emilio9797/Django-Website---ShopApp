from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'store'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id>/<slug:slug>/shop-detail', views.item_detail_view, name='shop-detail'),
    path('<int:id>/<slug:slug>/gallery-detail', views.gallery_detail_view, name='gallery-detail'),
    path('categories/<slug:slug>/', views.categories_view, name='category_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact-us/', views.contact_view, name='contact_view'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('shop/', views.shop_view, name='shop_view'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('thank-you/', views.tahnk_you_view, name='thank-you'),
    path('shop/<slug:slug>/', views.shop_category_view, name='shop_category_view')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)