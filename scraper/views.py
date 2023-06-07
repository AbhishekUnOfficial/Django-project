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
                search_results.append((names, links))  # Append each search result to the list

        return render(request, "scraper/search_results.html", {"results": search_results})

    return render(request, "scraper/search_form.html")


def skyscrape(request):
    if request.method == "POST":
        url = request.POST.get("link")  # Input is stored in the "url" variable
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        scraped_urls = set()

        hlinks = soup.select('a[href^="https://howblogs.xyz"]')

        for hlink in hlinks:
            hb = hlink.get('href')
            scraped_urls.add(hb)
        
        # Render the template with the scraped URLs as context
        return render(request, "scraper/skyscrape_output.html", {"scraped_urls": scraped_urls})
            
    return render(request, "scraper/search_form.html")  # Render the form template if not a POST request
    
