# from api_handler import NewsAPIClient
# from scraper import ArticleScraper

# class Aggregator:
#     def __init__(self):
#         self.api_client = NewsAPIClient()

#     def get_combined_data(self):
#         articles = self.api_client.fetch_articles()
#         for article in articles:
#             url = article.get('url')
#             scraper = ArticleScraper(url)
#             article['full_content'] = scraper.scrape_content()
#         return articles



from api_handler import NewsAPIClient
from scraper import ArticleScraper

class Aggregator:
    def __init__(self, category='technology'):
        self.api_client = NewsAPIClient(category=category)

    def get_combined_data(self):
        articles = self.api_client.fetch_articles()
        for article in articles:
            url = article.get('url')
            scraper = ArticleScraper(url)
            article['full_content'] = scraper.scrape_content()
        return articles