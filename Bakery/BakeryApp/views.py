from django.shortcuts import render
from django.http import HttpResponse



# Home/ index Section
def index(request):
    return render(request, 'BakeryApp/index.html')

# About Section
def about(request):
    return render(request, 'BakeryApp/about.html')

# Order Section
def order(request):
    return render(request, 'BakeryApp/order.html')

# Thank You for Order Form
def thanks_order(request):
    return render(request, 'BakeryApp/thanks_order.html')

# Contact Section
def contact(request):
    return render(request, 'BakeryApp/contact.html')
