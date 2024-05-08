import requests

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def movie_list(request):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        page_number = request.GET.get('page', 1)
    else:
        search_query = request.GET.get('query')
        page_number = request.GET.get('page', 1)

    api_key = '07caae28dab3a3943e0d33a58d4a88fc'
    base_url = 'https://api.themoviedb.org/3'

    if search_query:

        endpoint = '/search/movie'
        params = {
            'api_key': api_key,
            'query': search_query,
            'page': page_number
        }

    else:
        endpoint = '/discover/movie'
        params = {
            'api_key': api_key,
            'sort_by': 'popularity.desc',
            'page': page_number
        }
    response = requests.get(f'{base_url}{endpoint}', params=params)
    data = response.json()

    movies = data.get('results', [])
    total_pages = data.get('total_pages', 1)

    if int(page_number) > 1:
        prev_page = int(page_number) - 1
    else:
        prev_page = None
    if int(page_number) < int(total_pages):
        next_page = int(page_number) + 1
    else:
        next_page = None

    context = {
        'movies': movies,
        'search_query': search_query,
        'total_pages': total_pages,
        'next_page': next_page,
        'prev_page': prev_page,
        'page_number': page_number
    }

    return render(request, 'movies/index.html', context)


def movie_detail(request, movie_id):
    api_key = '07caae28dab3a3943e0d33a58d4a88fc'
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f"/movie/{movie_id}"
    params = {'api_key': api_key}
    response = requests.get(f'{base_url}{endpoint}', params=params)
    movie = response.json()
    context = {
        'movie': movie
    }

    return render(request, 'movies/detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')

    else:
        form = ContactForm(request.POST)
    return render(request, 'movies/contact.html', {'form': form})
