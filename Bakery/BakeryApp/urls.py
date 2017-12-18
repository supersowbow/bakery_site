from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('gallery/', views.gallery, name='gallery'),
    path('gallery/wedding/', views.gallery_wedding, name='gallery_wedding'),

    path('about/', views.about, name='about'),

    path('catering/', views.catering, name='catering'),

    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
]
