import requests,json
url='https://od-api.oxforddictionaries.com/api/v2/search/translations/en/es?q=hello'

def get_all_results(url):
    while url:
        r = requests.get(url)
        r.raise_for_status()
        for item in r.json()['results']:
            yield item
            url = r.links.get('next', {}).get('url')
            print(results)
