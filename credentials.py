import json

_API_CREDENTIALS_FILENAME = 'api_key.json'


def _import_api_credentials(file_name):
    """
    Imports JSON data from a local file.
    :param file_name: Name of the file to import from
    :return: Deserialized JSON data, else error
    """

    # read in the addresses from file
    try:
        with open(file_name) as f:
            deserialized_data = json.load(f)

        return deserialized_data['zoopla_api_key']
    except IOError:
        print ("Unable to API key file at %s. Please double check it's in the correct place and try again."
               % file_name)
        exit()
    except ValueError:
        print "Unable to interpret %s file as valid JSON." % file_name
        exit()

zoopla_api_key = _import_api_credentials(file_name=_API_CREDENTIALS_FILENAME)

