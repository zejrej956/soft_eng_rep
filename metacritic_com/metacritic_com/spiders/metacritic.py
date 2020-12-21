import scrapy
from scrapy import Request

class MetacriticSpider(scrapy.Spider):
    name = 'metacritic'
    # allowed_domains = ['metacritic.com']
    url = 'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=2019'

    def start_requests(self):
        return [Request(self.url, callback=self.parse_list_of_movies)]

    def parse_list_of_movies(self, response):
        pass
