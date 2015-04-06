# HouseBot

A tool to get notifications of the latest houses in your area with travel information to various locations.

## Setting up Dev environment
- create a new file api_key.json in the root directory of the project and add your Zoopla API key into it, i.e.

```
{
    "zoopla_api_key": "4adbe8c6dbe011e48ae714da"
}
```

- investigate config.py and update it with housing preferences relevant for you

- pip install -r requirements.txt

## Instructions
- Simply run housebot.py (any parameters for the listing details or age can be edited in manually housebot.py)
