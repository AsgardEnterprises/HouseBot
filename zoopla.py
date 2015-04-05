__author__ = 'Kadi'
import requests
import json
from datetime import datetime, time, timedelta

API_KEY_FILENAME = 'api_key.txt'
BASE_ZOOPLA_URI = 'http://api.zoopla.co.uk/api/v1/property_listings.js'  # remove '.js' for xml output

def get_properties(max_listing_age, params):
    # read in the API key
    with open(API_KEY_FILENAME) as f:
        api_key = f.readline()

    # construct the parameter string to include the parameters that have values
    param_string = ''
    for param in params:
        if params[param]:
            param_string += "{0}={1}&".format(param, params[param])

    # construct the url
    url = "{0}?{1}api_key={2}".format(BASE_ZOOPLA_URI, param_string, api_key)

    response = requests.get(url)
    json_response = response._content       # json string
    dict_data = json.loads(json_response)    # dictionary

    print('Url: ' + url)

    print('Total number of results: ' + str(dict_data['result_count']))

    # get cutoff date for desired listings
    now = datetime.now()
    min_listing_date = datetime.combine(now.date(), time(now.hour, now.minute)) + timedelta(minutes=-max_listing_age)

    print('Looking for listings that are posted after: {0} ({1} minutes)'.format(str(min_listing_date), max_listing_age))

    suitable_properties = []

    for listing in dict_data['listing']:
        date_published = datetime.strptime(listing['last_published_date'], '%Y-%m-%d %H:%M:%S')
        if min_listing_date < date_published:
            suitable_properties.append(listing)

    print('Found ' + str(len(suitable_properties)) + ' properties')

    for suitable_property in suitable_properties:
        print suitable_property

    return suitable_properties
