from django.shortcuts import render

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