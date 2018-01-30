from django.urls import path
from . import views

urlpatterns = [
    # Index Page
    path('', views.index, name='index'),

    # About Section
    path('about/', views.about, name='about'),

    # Order Section
    path('order/', views.order, name='order'),

    # Thank You Page for Order form
    path('thanks_order/', views.thanks_order, name='thanks_order'),

    # Contact Section
    path('contact/', views.contact, name='contact'),
]
