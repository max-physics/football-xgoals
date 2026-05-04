import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def load_competitions():
    BASE = Path("open-data/data/")
    with open(BASE / "competitions.json") as f:
        competitions = json.load(f)
    return competitions

def pass_locations(events):
    start_locations = []
    end_locations = []

    for event in events:
        event_type = event.get('type', {}).get('name')
        
        if event_type == 'Pass':
            start_locations.append(event.get('location'))
            end_locations.append(event.get('pass', {}).get('end_location'))

    return start_locations, end_locations

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

def shot_locations(events):
    start_locations = []
    end_locations = []

    for event in events:
        event_type = event.get('type', {}).get('name')
        
        if event_type == 'Shot':
            start_locations.append(event.get('location'))
            end_locations.append(event.get('shot', {}).get('end_location'))

    return start_locations, end_locations

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

def shot_distance(shot_start):
    x_middle_goal = 120
    y_middle_goal = 40
    distance = ((shot_start[0]-x_middle_goal)**2+(shot_start[1]-y_middle_goal)**2)**0.5
    return distance

