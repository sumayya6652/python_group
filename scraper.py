# from bs4 import BeautifulSoup
# import requests

# class ArticleScraper:
#     def __init__(self, url):
#         self.url = url

#     def scrape_content(self):
#         try:
#             response = requests.get(self.url)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             paragraphs = soup.find_all('p')
#             content = " ".join([p.text for p in paragraphs[:5]])
#             return content
#         except Exception as e:
#             return str(e)



from bs4 import BeautifulSoup
import requests

class ArticleScraper:
    def __init__(self, url):
        self.url = url

    def scrape_content(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            content = " ".join([p.text for p in paragraphs[:5]])
            return content
        except Exception as e:
            return str(e)