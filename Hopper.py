import requests
import json

url = "https://hopper.com/api/v4/shopSummary"

payload = json.dumps({
  "passengers": {
    "ADT": 1
  },
  "departureDate": "2024-02-07",
  "returnDate": "2024-02-15",
  "route": {
    "origin": {
      "regionType": "airport",
      "code": "DEL"
    },
    "destination": {
      "regionType": "airport",
      "code": "BLR"
    }
  },
  "tripFilter": "NoFilter",
  "platform": "Mobile"
})
headers = {
  'authority': 'hopper.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en, en',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'ajs_anonymous_id=d24a0a09-f97b-461b-bbb1-4468fcf0bddb; _gid=GA1.2.963814564.1706789818; _gat_UA-18588876-4=1; _gat_UA-18588876-13=1; _fbp=fb.1.1706789818444.1722664977; __ssid=54316e734dcfe7d3be2560550bd70e5; _dd_s=rum=0&expire=1706790726044; _ga_W2ZV1L1YD2=GS1.1.1706789817.1.1.1706789826.51.0.0; _ga=GA1.1.981609033.1706789818; Hopper-Session=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhY2Nlc3MiOiJleUpyYVdRaU9pSjJNU0lzSW5SNWNDSTZJa3BYVkNJc0ltRnNaeUk2SWtWVE1qVTJJbjAuZXlKMFpXNWhiblJmYVdRaU9pSm9iM0J3WlhJdFlYQndJaXdpYm05dVkyVWlPaTB5TWpBNE1UUXdNamMzT0RrME9Ua3lOelUyTENKMlpYSnphVzl1SWpvekxDSnphV1FpT2lJMU1UWmxZbUkyWXkwd05HWmxMVFE0TlRjdFlUZzBZaTB4WkRNME1XUTRZekUxTlRVaWZRLmVESDdCTEtrVU9ZWklyNDdoR1hidUZwQ0o2NHFLUGpoLXFzVENkdHBxYWg5Y1Q3a1gybERKaWctb0xfMExUWEhxRjU5Q2lZb1JvUG9FQ1dRRlRfdUZnIn0.tzXJlz81RUMOV-KmQrcDPm7KLnPk_Q4qOm_3WWRzxKcpA-dIVcEntYNkcWQOHvkB3L9KyTuwad2woiUBM3Ly8Q; _dd_s=rum=0&expire=1706790728684; Hopper-Session=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhY2Nlc3MiOiJleUpyYVdRaU9pSjJNU0lzSW5SNWNDSTZJa3BYVkNJc0ltRnNaeUk2SWtWVE1qVTJJbjAuZXlKMFpXNWhiblJmYVdRaU9pSm9iM0J3WlhJdFlYQndJaXdpYm05dVkyVWlPaTB5TWpBNE1UUXdNamMzT0RrME9Ua3lOelUyTENKMlpYSnphVzl1SWpvekxDSnphV1FpT2lJMU1UWmxZbUkyWXkwd05HWmxMVFE0TlRjdFlUZzBZaTB4WkRNME1XUTRZekUxTlRVaWZRLmVESDdCTEtrVU9ZWklyNDdoR1hidUZwQ0o2NHFLUGpoLXFzVENkdHBxYWg5Y1Q3a1gybERKaWctb0xfMExUWEhxRjU5Q2lZb1JvUG9FQ1dRRlRfdUZnIn0.tzXJlz81RUMOV-KmQrcDPm7KLnPk_Q4qOm_3WWRzxKcpA-dIVcEntYNkcWQOHvkB3L9KyTuwad2woiUBM3Ly8Q',
  'downlink': '10',
  'origin': 'https://hopper.com',
  'pragma': 'no-cache',
  'referer': 'https://hopper.com/flights/shop/?adultsCount=1&childrenCount&departureDate=2024-02-07&destination=BLR&flightShopProgress=1&flightShopType=default&infantsInSeatCount&infantsOnLapCount&noLCC=false&origin=DEL&returnDate=2024-02-15&stopsOption=ANY_NUMBER&tripCategory=round_trip&utm_source=hopper_web',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.234", "Google Chrome";v="120.0.6099.234"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-device-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJjbGllbnQtdXNlci1hZ2VudCI6Ik1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNyIsImNsaWVudC1pcCI6IjExNy4yMDMuMTk1LjEwMCJ9.hhNeMOUtSmVS_usZSNSyUCaluuKcWWe7MOyECmpPuXXW2ZE9yrLDP0C5DPglU-Wei9M5XQYkJKBhDJkrhnHxPw',
  'x-sec-ch-viewport-width': '911'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
