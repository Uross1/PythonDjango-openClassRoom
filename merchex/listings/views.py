from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})


def about(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/about-us.html',
                  {'bands': bands})


def listings(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'bands': bands})


def contact_us(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/contact.html',
                  {'bands': bands})
