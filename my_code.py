import json
import pandas as pd
import numpy as np

data = json.load(open('2022_JUNE.json', encoding='utf-8'))
time_list = []
place_list = []

for items in data.values():
    for item in items:
        for k in item.values():
            try:
                place_list.append(k['location']['name'])
            except:
                try:
                    place_list.append(k['location']['address'])
                except:
                    place_list.append(' ')
            time_list.append(k['duration']['startTimestamp'])

df = pd.DataFrame(place_list, time_list, columns=['Place'])
df.index = pd.to_datetime(df.index)
df['Date'] = df.index.date
df['Time'] = df.index.strftime('%H:%M')
df['Day'] = df.index.strftime('%A')
print(df.head())