import requests
import json
import time
import emailer

BASE_GOOGLE_MAPS_URI = 'https://maps.googleapis.com/maps/api/directions/json'


def get_time_to_work(selected_properties, addresses):
    email_message_body = ''

    # read each property
    for prop in selected_properties:
        email_message_body += 'Property address: ' + prop['displayable_address'] + '\n'
        email_message_body += 'Link: ' + 'http://www.zoopla.co.uk/to-rent/details/' + prop['listing_id'] + '\n'
        origin_address = prop['displayable_address'].replace(' ', '+')

        for address in addresses:
            email_message_body += address + ' travel: ' + '\n'
            destination_address = addresses[address].replace(' ', '+')
            url_driving = '{0}?origin={1}&destination={2}'.format(BASE_GOOGLE_MAPS_URI, origin_address, destination_address)
            dict_data = send_request(url_driving)
            email_message_body += ('Driving: {0} ({1})'.format(dict_data['routes'][0]['legs'][0]['duration']['text'],
                                                               dict_data['routes'][0]['legs'][0]['distance']['text']) + '\n')
            url_transit = '{0}?origin={1}&destination={2}&mode=transit'.format(BASE_GOOGLE_MAPS_URI,
                                                                               origin_address, destination_address)
            dict_data = send_request(url_transit)
            email_message_body += 'Transit: {0} ({1})'.format(dict_data['routes'][0]['legs'][0]['duration']['text'],
                                              dict_data['routes'][0]['legs'][0]['distance']['text']) + '\n'
        email_message_body += '\n'
    # send email notifying that new properties have been found
    print(email_message_body)
    emailer.send_notification_emails(email_message_body)


def send_request(url):
    """
    Google Maps limits searches to 10 per second.
    If limit is reached, wait 2 seconds and retry
    :param url:
    :return:
    """
    response = requests.get(url)
    dict_data = json.loads(response.content)
    if dict_data['status'] == 'OVER_QUERY_LIMIT':
        time.sleep(2)
        response = requests.get(url)
        dict_data = json.loads(response.content)

    if dict_data['status'] == 'OVER_QUERY_LIMIT':
        time.sleep(2)
        response = requests.get(url)
        dict_data = json.loads(response.content)

    return dict_data
