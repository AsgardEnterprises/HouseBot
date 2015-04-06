import json

_API_CREDENTIALS_FILENAME = 'credentials.json'


def _import_api_credentials(file_name, item):
    """
    Imports JSON data from a local file.
    :param file_name: Name of the file to import from
    :return: Deserialized JSON data, else error
    """

    # read in the addresses from file
    try:
        with open(file_name) as f:
            deserialized_data = json.load(f)

        return deserialized_data[item]
    except IOError:
        print ("Unable to API key file at %s. Please double check it's in the correct place and try again."
               % file_name)
        exit()
    except ValueError:
        print "Unable to interpret %s file as valid JSON." % file_name
        exit()

zoopla_api_key = _import_api_credentials(file_name=_API_CREDENTIALS_FILENAME, item='zoopla_api_key')
gmail_address = _import_api_credentials(file_name=_API_CREDENTIALS_FILENAME, item='gmail_address')
gmail_password = _import_api_credentials(file_name=_API_CREDENTIALS_FILENAME, item='gmail_password')

