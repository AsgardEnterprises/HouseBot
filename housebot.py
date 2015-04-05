__author__ = 'Kadi'
import zoopla
import google_maps

import config

# Find all properties that match our housing requirements
matching_properties_zoopla = zoopla.get_properties(
    max_listing_age=config.house_maximum_listing_age,
    params=config.house_search_parameters
)

# Find the group's commute time to all properties that passed the filtering process.
matching_properties = google_maps.get_time_to_work(
    selected_properties=matching_properties_zoopla,
    addresses=config.house_member_commuting_destinations
)