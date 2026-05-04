import numpy as np
import matplotlib.pyplot as plt 
import sys
print(sys.executable)
import json
from pathlib import Path
from analysis import load_competitions

def print_matches(selected_comp):
    match_data = matches(selected_comp)
    match_dict = {
        f'{m['home_team']['home_team_name']} vs. {m['away_team']['away_team_name']}':m['match_id']
        for m in match_data
    }
    return match_dict

BASE = Path("open-data/data/")

competitions = load_competitions()

shot_events = []

for comp in competitions:
    s_id = comp['season_id']
    with open(BASE / "matches" / str(comp.get('competition_id')) / f'{s_id}.json') as f:
        matches = json.load(f)
    for m in matches:
        match_id = m['match_id']
        with open(BASE / "events" / f"{match_id}.json") as f:
            events = json.load(f)

        for event in events:
            event_type = event.get('type', {}).get('name')
            if event_type == 'Shot':
                shot_events.append(event)


from analysis import pass_locations, plot_passes, shot_locations, plot_shots, shot_distance

shot_locations = shot_locations(shot_events)

def goal_no_goal(events):

    goals = []

    for event in events:
        event_type = event.get('type', {}).get('name')
        
        if event_type == 'Shot':
            if event.get('shot',{}).get('outcome',{}).get('name') == 'Goal':
                goals.append(1)
            else:
                goals.append(0)
    return goals

#print(goal_no_goal(shot_events))

#print(shot_locations[0])
distances = []
for shots in shot_locations[0]:
    distances.append(shot_distance(shots))

#print(distances)


plt.hist(goal_no_goal(shot_events), distances)
plt.show()

