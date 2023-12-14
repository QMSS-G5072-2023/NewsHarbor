import requests
import pandas as pd

class NewsharborAPI:
    def __init__(self):
        self.api_key = '7a4f1oelyBGs9zmYKxk4lWm2cziztmS7'
        self.base_url = 'https://api.nytimes.com/svc/news/v3/content/'

    def get_section_list(self):
        section_list_endpoint = 'section-list.json'
        response = requests.get(f'{self.base_url}{section_list_endpoint}', params={'api-key': self.api_key})
        try:
            response.raise_for_status()
            # Return the response JSON data directly
            return response.json()
        except requests.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Other error occurred: {err}"

    #Get the latest news
    def get_latest_news(self, section, limit=10):
        endpoint = f'{section}.json'
        response = requests.get(f'{self.base_url}{endpoint}', params={'api-key': self.api_key, 'limit': limit})
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Other error occurred: {err}"

    #Search the news
    def search_news(self, query, limit=10):
        endpoint = 'all.json'
        response = requests.get(f'{self.base_url}{endpoint}', params={'api-key': self.api_key, 'q': query, 'limit': limit})
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Other error occurred: {err}"

    #get news details
    def get_news_details(self, url):
        response = requests.get(url)
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Other error occurred: {err}"

    #analyze news data
    def analyze_news_data(self, section):
        data = self.get_latest_news(section)
        df = pd.json_normalize(data['results'])

