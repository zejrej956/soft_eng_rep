# -*- coding: utf-8 -*-
import os
import pytest
from scrapy.utils.test import get_crawler
from scrapy_tdd import *
from scrapy.exceptions import CloseSpider

from .metacritic import MetacriticSpider

def response_from(file_name, url="https://metacritic.com"):
    return mock_response_from_sample_file(my_path(__file__) + "/samples", file_name, url=url)

def describe_metacritic_spider():
    to_test = MetacriticSpider().from_crawler(get_crawler())
    r = to_test.start_requests()

    # def describe_list_of_movies():
    resp = response_from("list_of_movies.html", url="https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=2019")
    results = to_test.parse_list_of_movies(resp)
    print(results)

    def should_return_number_of_movies():
        assert len(results) == 100