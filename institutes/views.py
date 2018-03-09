# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from utils import get_url, get_data_from_google_api
from settings import GOOGLE_SEARCH_PARAMS, GOOGLE_PLACE_URL, GOOGLE_PLACE_PARAMS, GOOGLE_SEARCH_URL, LOCATION
import json
import requests


def institutes(request):

    if request.method == "GET":
        data = {
            "result": [],
            "next_page_token": "",
            "error": 0,
            "error_msg": ""
        }
        try:
            place_urls = []
            output = []
            location = request.GET.get('location', '')
            if location == '':
                raise Exception("please enter a location")
            next_page = request.GET.get('next', '')
            if next_page:
                GOOGLE_SEARCH_PARAMS.update({"pagetoken": next_page})
            GOOGLE_SEARCH_PARAMS.update({"location": LOCATION.get(location)})
            search_url = get_url(GOOGLE_SEARCH_URL, GOOGLE_SEARCH_PARAMS)
            response = requests.get(search_url)
            if response.status_code == 200:
                places = (response.json()).get('results')
                data['next_page_token'] = (response.json()).get('next_page_token')
                for place in places:
                    GOOGLE_PLACE_PARAMS.update({"placeid": place.get('place_id')})
                    place_url = get_url(GOOGLE_PLACE_URL, GOOGLE_PLACE_PARAMS)
                    place_urls.append(place_url)
            place_results = get_data_from_google_api(place_urls)
            for place in place_results:
                if place.status_code == 200:
                    result = {}
                    institute = (place.json()).get('result')
                    result["name"] = institute.get('name')
                    result["website"] = institute.get('website')
                    result["address"] = institute.get('formatted_address')
                    result["contact"] = institute.get('formatted_phone_number')
                    output.append(result)
                data['result'] = output
        except Exception as e:
            data['error'] = 1
            data['error_msg'] = e.__str__()

        finally:
            GOOGLE_SEARCH_PARAMS.pop('pagetoken', '')
            json_output = json.dumps(data, indent=2)
            return HttpResponse(json_output, content_type="application/json")
