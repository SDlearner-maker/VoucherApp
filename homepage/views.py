from django.shortcuts import render


# Create your views here.
def home(requests):
    return render(requests, 'homepage/home.htm')


def about(requests):
    return render(requests, 'homepage/about.htm', {'title': 'about'})