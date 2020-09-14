from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/', views.add_view, name='add_view'),
    path('add_onchange/<int:item_id>/', views.add_view, name='onchange_add_view'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove')

]
