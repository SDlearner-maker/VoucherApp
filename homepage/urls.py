from django.urls import path
from . import views
# url page for the homepage
urlpatterns = [
   path('', views.home, name='voucher-homepage'),
   path('about/', views.about, name='voucher-about')
]
