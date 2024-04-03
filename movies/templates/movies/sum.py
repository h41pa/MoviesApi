import requests
from django.shortcuts import render, get_object_or_404


def movie_list(request):
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
    prev_page = int(page_number) - 1 if int(page_number) > 1 else None
    next_page = int(page_number) + 1 if int(page_number) < total_pages else None

    return render(request, 'movies/index.html',
                  {'movies': movies, 'search_query': search_query, 'total_pages': total_pages,
                   'prev_page': prev_page, 'next_page': next_page, 'page_number': page_number})


def movie_detail(request, movie_id):
    api_key = '07caae28dab3a3943e0d33a58d4a88fc'
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f'/movie/{movie_id}'
    params = {
        'api_key': api_key,
    }

    response = requests.get(f'{base_url}{endpoint}', params=params)
    movie = response.json()

    return render(request, 'movies/detail.html', {'movie': movie})
