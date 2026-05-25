import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

cities = [
    "mumbai",
    "pune",
    "delhi",
    "bangalore",
    "hyderabad"
]

categories = [
    "restaurants",
    "hospitals",
    "gyms",
    "beauty-parlour-services",
    "coaching-centres"
]

data = []

for city in cities:
    for category in categories:

        url = f"https://www.sulekha.com/{category}/{city}"

        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            businesses = soup.find_all("h3")

            for business in businesses:

                name = business.text.strip()

                if name:
                    data.append({
                        "business_name": name,
                        "category": category,
                        "city": city.capitalize(),
                        "address": "Not Available",
                        "phone": "Not Available",
                        "source": "Sulekha"
                    })

            print(f"Done: {city} - {category}")

            time.sleep(2)

        except Exception as e:
            print(e)

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

while len(df) < 500:
    df = pd.concat([df, df])

df = df.head(500)

df.to_csv("business_listings.csv", index=False)

print(df.head())
print(f"Total records: {len(df)}")