from django.urls import path
from . import views

urlpatterns = [
    path('', views.skysearch, name='skysearch'),
    path('scrape/', views.skyscrape, name='skyscrape')
]

