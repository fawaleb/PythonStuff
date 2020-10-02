import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.20034000000004&lon=-119.18011999999999#.X3RIpBTiuMo')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-container')
items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items[1:]]
short_descs = [item.find(class_='short-desc').get_text() for item in items[1:]]
temperatures = [item.find(class_='temp').get_text() for item in items[1:]]

weather=pd.DataFrame(
    {'Period':period_names,
     'Short Descriptions':short_descs,
     'Temperature':temperatures}
)

weather.to_csv('weather.csv')

print(weather)