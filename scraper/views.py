from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Movie

def scrape_home_page():
    url = "https://skymovieshd.wine/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    clinks = []
    cnames = []

    for bolly in soup.find_all("div", class_="Bolly"):
        for atags in bolly.find_all("a"):
            clinks.append(url + atags.get("href"))
            cnames.append(atags.text)

    return clinks, cnames

def home(request):
    clinks = []
    cnames = []
    movies = Movie.objects.all()
    for movie in movies:
        clinks.extend(movie.links.split(','))
        cnames.extend(movie.name.split(','))
    zipped_links_and_names = zip(clinks, cnames)
    return render(request, "scraper/index.html", {'zipped_links_and_names': zipped_links_and_names, 'movies': movies})

def scrape_recent_movies():
    url = "https://skymovieshd.gold/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    movies = []

    for links in soup.find_all("div", class_="Fmvideo"):
        for link in links.find_all("a"):
            movies.append(url + link.get("href"))

    return movies

def recent_movies(request):
    movies = scrape_recent_movies()
    return render(request, "scraper/index.html", {"movies": movies})

def search(request):
    content_name = request.GET.get('content_name')
    domain = 'https://skymovieshd.gold'
    url = f"{domain}/search.php?search={content_name}&cat=All"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    search_results = []

    for search_result in soup.find_all('div', class_='L'):
        for atags in search_result.find_all('a'):
            search_results.append(domain + atags.get('href'))

    return render(request, 'scraper/search.html', {'search_results': search_results})

