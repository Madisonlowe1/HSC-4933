import requests

# A Census API URL always has this shape:
# https://api.census.gov/data/{year}/{dataset}?get={variables}&for={geography}


YEAR = 2020
DATASET = "dec/pl"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "075b7b28bf72d9c67bef15613482981bf7fe37bb"

params = {
    "get": "NAME,P1_001N",
    "for": "state:*",
    "key": API_KEY,
}


response = requests.get(URL, params=params)
response.raise_for_status()

if response.status_code != 200:
    print(f"response failed({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()


print(f"Got {len(data) - 1} rows back.")

for i in data:
    print(i)


