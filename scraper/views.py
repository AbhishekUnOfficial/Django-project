import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def skysearch(request):
    if request.method == "POST":
        content_name = request.POST.get("content_name")
        domain = "https://skymovieshd.gold"
        url = f"{domain}/search.php?search={content_name}&cat=All"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        search_results = []  # Create an empty list to store the search results

        for search_result in soup.find_all("div", class_="L"):
            for atags in search_result.find_all("a"):
                links = domain + atags.get("href")
                names = atags.text.strip()
                search_results.append(
                    (names, links)
                )  # Append each search result to the list

        return render(
            request, "scraper/search_results.html", {"results": search_results}
        )

    return render(request, "scraper/search_form.html")


def skyscrape(request):
    if request.method == "POST":
        url = request.POST.get("link")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        for l in soup.select('a[href^="https://hblogs.xyz"]'):
            return render(request, "scraper/hpage.html")
