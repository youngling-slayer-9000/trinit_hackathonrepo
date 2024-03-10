from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name='home'),
   path('result',views.result,name = 'result'),
   path('webpage',views.webpage,name = 'webpage'),
    path('registration/', views.registration, name='register'),
    path('tutor_registration/', views.tutor_registration, name='tutor_registration')


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)