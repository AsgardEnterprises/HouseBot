# HouseBot

A tool to get notifications of the latest houses in your area with travel information to various locations.

## Setting up Dev environment
- create a new file credentials.json in the root directory of the project and add your Zoopla API key and gmail 
credentials into it, i.e.

```
{
    "zoopla_api_key": "4adbe8c6dbe011e48ae714da",
    "gmail_address": "something@gmail.com",
    "gmail_password": "password"
}
```

- investigate config.py and update it with housing preferences relevant for you (add emails of all the people who
want to be notified when new houses are found in the house_member_email_addresses in JSON format, i.e
```
{
    "email": "email@gmail.com",
    "email2": "email2@gmail.com"
}
```

- pip install -r requirements.txt

## Instructions
- Simply run housebot.py (any parameters for the listing details or age can be edited in manually housebot.py)
