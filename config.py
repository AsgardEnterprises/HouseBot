"""
This module provides configurable parameters which let the user
tailor HouseBot's results to their preferences.
"""

# A number of house specified attributes you can tune to
# find the breed of property you want to call your home.
house_search_parameters = {
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

# The maximum amount of time a property has been
# 'live' for. Any properties that have been up for
# longer are not included in the search. This is because
# the searches will be conducted periodically and we don't
# want to be swamped by 'old' results
house_maximum_listing_age = 60 * 12  # In minutes


# Warning! Since this is stored in a dictionary later, house member name must be unique!
# Work (or other destination!) addresses of the household-members-to-be.
# HouseBot will check the travel time to each destination below
# for each property that passes the search filtering.
# the emails will be used to notify if a new house is available
house_member_details = [
    {
        "name": "Alice",
        "commute_destination": "221B Baker Street",
        "email_address": "alice@useagmailaddress.com",
        "max_commute_time_in_minutes": 45
    },
    {
        "name": "Bob",
        "commute_destination": "221B Baker Street",
        "email_address": "bob@useagmailaddress.com",
        "max_commute_time_in_minutes": 30
    }
]
