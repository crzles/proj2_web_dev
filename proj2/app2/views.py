from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import (
    Slider,
    SocialLink,
    MovieTheater,
    MovieTV,
    Advertisement,
    Celebrity,
    Trailer,
    TrailerItem,
    News,
    Tweet,
    NewsletterSubscriber,
)


def home(request):
    context = {
        'sliders': Slider.objects.all(),
        'social_links': SocialLink.objects.all(),

        'theater_movies': MovieTheater.objects.all(),
        'tv_movies': MovieTV.objects.all(),

        'sidebar_ads': Advertisement.objects.filter(section='sidebar'),
        'celebrities': Celebrity.objects.all(),

        'trailers': Trailer.objects.all(),
        'trailer_items': TrailerItem.objects.all(),

        'news_ad': Advertisement.objects.filter(section='news').first(),
        'main_news': News.objects.filter(section='main').first(),
        'more_news': News.objects.filter(section='more'),
        'tweets': Tweet.objects.all(),
    }

    return render(request, 'app2/index.html', context)


def moviesingle(request):
    return render(request, 'app2/moviesingle.html')


def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)

    return redirect('home')


def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

    return redirect('home')




def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

    return redirect('home')