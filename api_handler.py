# import requests
# from config import API_KEY, BASE_URL

# class NewsAPIClient:
#     def __init__(self, country='us', category='technology'):
#         self.country = country
#         self.category = category

#     def fetch_articles(self):
#         params = {
#             'apiKey': API_KEY,
#             'country': self.country,
#             'category': self.category,
#             'pageSize': 10
#         }
#         response = requests.get(BASE_URL, params=params)
#         data = response.json()
#         return data.get('articles', [])




import requests
from config import API_KEY, BASE_URL

class NewsAPIClient:
    def __init__(self, country='us', category='technology'):
        self.country = country
        self.category = category

    def fetch_articles(self):
        params = {
            'apiKey': API_KEY,
            'country': self.country,
            'category': self.category,
            'pageSize': 10
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        return data.get('articles', [])