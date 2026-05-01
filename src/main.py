import sys
print(sys.executable)

import json
from pathlib import Path




def load_competitions():
    BASE = Path("open-data/data/")
    with open(BASE / "competitions.json") as f:
        competitions = json.load(f)
    return competitions



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

def plot_passes(pass_start, pass_end):
    fig, ax = plt.subplots(figsize=(10, 7))

    pitch = patches.Rectangle((0, 0), 120, 80,
                                edgecolor='black',
                                facecolor='green',
                                linewidth=2)
    ax.add_patch(pitch)
    #for i in range(len(pass_start)):
     #   ax.plot([pass_start[i][0], pass_end[i][0]],[pass_start[i][1], pass_end[i][1]])

    for start, end in zip(pass_start, pass_end):
        ax.plot([start[0], end[0]], [start[1], end[1]])
    
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')

    plt.show()
    return fig

#plot_passes(pass_start, pass_end)
shots_timestamp = [
    event.get('index', {})
    for event in events
    if event.get('type', {}).get('name') == 'Shot'
]

print(shots_timestamp)

print(events[435])

def shot_locations(events):
    start_locations = []
    end_locations = []

    for event in events:
        event_type = event.get('type', {}).get('name')
        
        if event_type == 'Shot':
            start_locations.append(event.get('location'))
            end_locations.append(event.get('shot', {}).get('end_location'))

    return start_locations, end_locations

shot_start, shot_end = shot_locations(events)

def plot_shots(shot_start, shot_end):
    fig, ax = plt.subplots(figsize=(10, 7))

    pitch = patches.Rectangle((0, 0), 120, 80,
                                edgecolor='black',
                                facecolor='green',
                                linewidth=2)
    ax.add_patch(pitch)
    #for i in range(len(pass_start)):
     #   ax.plot([pass_start[i][0], pass_end[i][0]],[pass_start[i][1], pass_end[i][1]])

    for start, end in zip(shot_start, shot_end):
        ax.plot([start[0], end[0]], [start[1], end[1]])
    
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')

    plt.show()
    return fig

#plot_shots(shot_start, shot_end)

print(competitions[0])

def competition_year(competitions):
    name_year = []
    for competition in competitions:
        name_year.append(competition.get('competition_name')+competition.get('season_name'))
    
    return name_year
            
print(competition_year(competitions))
