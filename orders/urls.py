from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path('cart', views.cart, name='cart'),
   path('add_to_cart', views.add_to_cart, name='add_to_cart'),
   path('remove_from_cart/<id>"',views.remove_from_cart, name='remove_from_cart'),
   path('increase_quntity/<id>',views.increase_quntity,name='increase_quntity'),
   path('decrease_quntity/<id>',views.decrease_quntity,name='decrease_quntity'),
   path('checkout',views.checkout,name='checkout'),
   path('order',views.order,name='order')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)