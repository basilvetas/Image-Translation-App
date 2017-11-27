import requests

def test():
    q = ["artichoke", "salad", "tomatoes"]
    source = 'en'
    target = 'fr'


    url = 'http://localhost:5001/'
    data = {
              'q': q, # string or list of strings
              'source': source,
              'target': target,
            }

    r = requests.get(url=url, data=data)

    print(r.json())

test()