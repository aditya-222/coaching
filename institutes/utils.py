import grequests
from urllib import urlencode


def get_url(url, params):
    encoded_params = urlencode(params)
    url = url + encoded_params
    return url


def get_data_from_google_api(urls):
    response = (grequests.get(url) for url in urls)
    data = grequests.map(response)
    return data