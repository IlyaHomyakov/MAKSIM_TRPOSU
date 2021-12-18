from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def main(request):
    context = {
        'films_in_rent_number': len(Film.objects.filter(is_film_in_rent=True)),
        'popular_films': Film.objects.filter(is_film_in_rent=True).order_by('-id'),
    }

    return render(request, 'afisha/main.html', context)


def film(request, film_id):
    if request.POST:
        film_id = request.path[-2]
        print(request.path[-2])
        author = request.POST['name']
        text = request.POST['review']
        Review.objects.create(
            review_author=author,
            review_film=get_object_or_404(Film, pk=film_id),
            review_text=text
        ).save()
        return redirect(f'http://127.0.0.1:8000{request.path}')
    context = {
        'film': get_object_or_404(Film, pk=film_id),
        'schedule': Show.objects.filter(show_film_id=film_id, show_date__gte=timezone.now()).order_by('show_date'),
        'reviews': Review.objects.filter(review_film=film_id)
    }
    return render(request, 'afisha/film.html', context)
