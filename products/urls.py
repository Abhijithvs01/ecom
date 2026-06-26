from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('products',views.product, name='products'),
    path('detail_product/<id>',views.deatil_product, name='detail_product'),
    path('search',views.product_search,name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)