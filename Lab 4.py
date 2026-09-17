import requests

YEAR = 2020
DATASET = "dec/pl"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "075b7b28bf72d9c67bef15613482981bf7fe37bb"

print("Census API")

State = input("State FIPS codes (* for all, or 06): ").strip()

Variables = input("Variables").strip()

params = {
    "get": Variables,
    "for": f"state:{State}",
    "key": API_KEY,
}

response = requests.get(URL, params=params)

if response.status_code != 200:
    print(f"response failed({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()

print(f"Got {len(data)} Rows of Data.")

for i in data:
    print(i)

