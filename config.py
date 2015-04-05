"""
This module serves to import user configurable data such as
addresses of private API keys and provide them to HouseBot.
"""
import json

# Edit these two values with the location of your appropriate file.
API_KEY_FILENAME = 'api_key.json'
ADDRESSES_FILENAME = 'addresses.json'


def _import_data_from_json_file(file_name):
    """
    Imports JSON data from a local file.
    :param file_name: Name of the file to import from
    :return: Deserialized JSON data, else error
    """

    # read in the addresses from file
    try:
        with open(file_name) as f:
            deserialized_data = json.load(f)

        return deserialized_data
    except IOError:
        print ("Unable to find addresses. "
               "Please ensure you have a %s file in the root directory"
               % file_name)
        exit()
    except ValueError:
        print "Unable to interpret %s file as valid JSON." % file_name
        exit()


user_addresses = _import_data_from_json_file(file_name=ADDRESSES_FILENAME)
zoopla_api_key = _import_data_from_json_file(file_name=API_KEY_FILENAME)["zoopla_api_key"]
