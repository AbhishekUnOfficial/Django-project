import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def skysearch(request):
    if request.method == "POST":
        content_name = request.POST.get("content_name")
        domain = "https://skymovieshd.date"
        url = f"{domain}/search.php?search={content_name}&cat=All"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        search_results = [(domain + atag.get("href"), atag.text.strip()) for atag in soup.select("div.L a")]

        return render(request, "scraper/search_results.html", {"results": search_results})

    return render(request, "scraper/search_form.html")


def skyscrape(request):
    if request.method == "POST":
        url = request.POST.get("link")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        scraped_data = []
        scraped_links = set()

        for atag in soup.select('a[href^="https://howblogs.xyz"]'):
            link = atag.get("href")
            name = atag.text.strip()
            if link not in scraped_links:
                scraped_data.append((link, name))
                scraped_links.add(link)

        return render(request, "scraper/skyscrape_output.html", {"scraped_data": scraped_data})

    return render(request, "scraper/search_form.html")
    