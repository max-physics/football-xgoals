import sys
print(sys.executable)

import json
from pathlib import Path

BASE = Path("open-data/data/")


with open(BASE / "competitions.json") as f:
    competitions = json.load(f)

bundesliga = [
    c for c in competitions
    if c["competition_name"] == "1. Bundesliga"
]

with open(BASE / "matches" / "9" / "281.json") as f:
    matches = json.load(f)


matches_0 = matches[0]

match_id = matches_0['match_id']

with open(BASE / "events" / f"{match_id}.json") as f:
    events = json.load(f)


match_id = matches_0['match_id']

with open(BASE / "events" / f"{match_id}.json") as f:
    events = json.load(f)


#print(events[0])
for i in range(len(events)):
    if events[i]['type']['name'] == 'Pass':
        print(events[i]['type']['name'])

passes_timestamp = [
    event.get('timestamp', {})
    for event in events
    if event.get('type', {}).get('name') == 'Pass'
]

#print(passes_timestamp)

def passes_time(events):
    passes_timestamp = [
        event.get('timestamp')
        for event in events
        if event.get('type', {}).get('name') == 'Pass'
    ]
    return passes_timestamp
'''
def pass_locations(events):
    start_locations = [
        event.get('location')
        for event in events
        if event.get('type', {}).get('name') == 'Pass'  
    ]
    end_locations = [
        event.get('pass', {}).get('end_location')
        for event in events
        if event.get('type', {}).get('name') == 'Pass'
    ]

    return start_locations, end_locations

print(pass_locations(events))
print(events[7])
'''
def pass_locations(events):
    start_locations = []
    end_locations = []

    for event in events:
        event_type = event.get('type', {}).get('name')
        
        if event_type == 'Pass':
            start_locations.append(event.get('location'))
            end_locations.append(event.get('pass', {}).get('end_location'))

    return start_locations, end_locations

pass_start, pass_end = pass_locations(events)

print(pass_start[0][0])
# initailize the field

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 7))

pitch = patches.Rectangle((0, 0), 120, 80,
                            edgecolor='black',
                            facecolor='green',
                            linewidth=2)

for i in range(len(pass_start)):
    ax.plot([pass_start[i][0], pass_end[i][0]],[pass_start[i][1], pass_end[i][1]])

ax.add_patch(pitch)

#ax.set_xlim(0, 120)
#ax.set_ylim(0, 80)
ax.set_aspect('equal')

plt.show()

