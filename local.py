import requests
from fastapi import FastAPI
def display_alert(feature):
    print(f"Type: {feature['properties']['@type']}\n"
          f"Area: {feature['properties']['areaDesc']}\n"
          f"Status: {feature['properties']['status']}\n"
          f"Severity: {feature['properties']['severity']}\n"
          f"Certainty: {feature['properties']['certainty']}\n"
          f"Urgency: {feature['properties']['urgency']}\n")
    print(f"++++ Update ++++\n"
          f"{feature['properties']['headline']}\n"
          f"{feature['properties']['description']}\n"
          f"{feature['properties']['instruction']}\n\n")


def run_code():
    cities = ["AL", "AK", "AS", "AR", "AZ", "CA", "CO", "CT", "DE", "DC",
              "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
              "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
              "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VI",
              "VA", "WA", "WV", "WI", "WY", "MP", "PW", "FM", "MH"]
    chosen = ''
    url="https://api.weather.gov/alerts/active?area="

    print("++ Alerts Updater ++\n")
    print("Choose a city: \n")
    for i in range(0, len(cities), 2):
        left = f"{i + 1}. {cities[i]}"
        if i + 1 < len(cities):
            right = f"{i + 2}. {cities[i + 1]}"
        else:
            right = ""
        print(f"{left:<20} {right}")

    chosen_num = int(input("Choose a city:"))
    chosen_num -= 1
    chosen = str(cities[chosen_num])
    url = str(url+chosen)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['title'])
        if data['features'] == []:
            print("No alerts")
        else:
            for feature in data['features']:
                display_alert(feature)
    else:
        print("ERROR")


run_code()