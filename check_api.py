import requests
from fastapi import FastAPI

app = FastAPI()


def display_alert(feature):
    return {
        "type": feature['properties']['@type'],
        "area": feature['properties']['areaDesc'],
        "status": feature['properties']['status'],
        "severity": feature['properties']['severity'],
        "certainty": feature['properties']['certainty'],
        "urgency": feature['properties']['urgency'],
        "headline": feature['properties']['headline'],
        "description": feature['properties']['description'],
        "instruction": feature['properties']['instruction']
    }

@app.get("/alerts/{state_code}")
def get_alerts(state_code: str):
    url = f"https://api.weather.gov/alerts/active?area={state_code}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error"

    data = response.json()
    print(data['title'])
    if data['features'] == []:
        print("No alerts")
    else:
        for feature in data['features']:
            display_alert(feature)

