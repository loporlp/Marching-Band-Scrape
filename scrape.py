import json
import requests

URL = "https://www.umea.us/mb-scores"
page = requests.get(URL)

import requests

from bs4 import BeautifulSoup

headers = {
    'authority': 'bridge.competitionsuite.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www-umea-us.filesusr.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = {
    'competition': '4af3a3ef-666f-401d-9901-bed45252ef32',
    'version': '1.1.5',
    'callback': 'jQuery110204313023920818535_1662597435203',
    '_': '1662597435211',
}

response = requests.get('https://bridge.competitionsuite.com/api/orgscores/GetCompetition/jsonp', params=params, headers=headers)

print(response.text)
res = json.loads(response.text)



for name, score in res:
    print(name)