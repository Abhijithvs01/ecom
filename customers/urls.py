from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path('account', views.login_page , name= 'account'),
   path('register', views.register, name='register'),
   path('logout',views.sign_out, name='logout'),
   path('profile',views.profile,name='profile'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)