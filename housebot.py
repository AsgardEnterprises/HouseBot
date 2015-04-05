__author__ = 'Kadi'
import zoopla
import google_maps
import json

ADDRESSES_FILENAME = 'addresses.json'

max_listing_age = 60*12  # in minutes

# construct params
params = {
    'order_by': 'age',          # price, age
    'ordering': '',             # descending (default), ascending
    'listing_status': 'rent',
    'area': 'London',
    'minimum_price': '300',     # price per week
    'maximum_price': '400',     # price per week
    'minimum_beds': '3',
    'maximum_beds': '4',
    'furnished': '',            # furnished, unfurnished, part-furnished
    'property_type': '',        # houses, flats
    'page_number': '',          # the page number of results to request, default 1
    'page_size': '100'          # the size of each page of results, default 10, maximum 100
}

# read in the addresses from file
with open(ADDRESSES_FILENAME) as f:
    json_addresses = f.read()

addresses = json.loads(json_addresses)

matching_properties_zoopla = zoopla.get_properties(max_listing_age, params)
matching_properties = google_maps.get_time_to_work(matching_properties_zoopla, addresses)