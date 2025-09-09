# weather_dashboard.py
import requests, json
from pathlib import Path

API_KEY = "YOUR_OPENWEATHER_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
HISTORY_FILE = Path("history.json")

def get_weather(city):
    resp = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Error:", resp.json().get("message", resp.status_code))
        return None

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []

def save_history(hist):
    with open(HISTORY_FILE, "w") as f:
        json.dump(hist, f, indent=2)

def main():
    history = load_history()
    while True:
        print("\n1: Search city | 2: Show last 5 | 3: Quit")
        c = input("Choice: ").strip()
        if c == "1":
            city = input("City name: ")
            data = get_weather(city)
            if data:
                print(f"{data['name']}: {data['weather'][0]['description'].title()}, {data['main']['temp']}°C")
                history.append({"city": city, "data": data})
                save_history(history)
        elif c == "2":
            for entry in history[-5:]:
                print(entry["city"])
        else:
            break

if __name__ == "__main__":
    main()
      
