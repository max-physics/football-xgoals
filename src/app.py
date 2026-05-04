import streamlit as st
from analysis import load_competitions
import json
from pathlib import Path
import matplotlib.pyplot as plt


st.title("FOOTBALL STATISTICS")

BASE = Path("open-data/data/")

competitions = load_competitions()

def competition_year(competitions):
    name_year = []
    for competition in competitions:
        name_year.append(competition.get('competition_name')+competition.get('season_name'))
    
    return name_year
            
name_year = competition_year(competitions)

selected_comp = st.selectbox(
    "Available Competitions",
    name_year
)

st.write(f"Chosen competition: {selected_comp}")

def matches(selected_comp):
    year = selected_comp[-9:]
    name = selected_comp[:-9]
    for competition in competitions:
        if year == competition.get('season_name') and name == competition.get('competition_name'):
            s_id = competition.get('season_id')
            with open(BASE / "matches" / str(competition.get('competition_id')) / f'{s_id}.json') as f:
                matches = json.load(f)
            
            
    return matches



def print_matches(selected_comp):
    match_data = matches(selected_comp)
    match_dict = {
        f'{m['home_team']['home_team_name']} vs. {m['away_team']['away_team_name']}':m['match_id']
        for m in match_data
    }
    return match_dict

if selected_comp:
    match_names = print_matches(selected_comp)
    selected_match = st.selectbox(
    "Available matches",
    list(match_names.keys())
    )

if selected_match:
    st.write(match_names[selected_match])


def load_events(match_id):
    with open(BASE / "events" / f"{match_id}.json") as f:
        events = json.load(f)
    return events

from analysis import pass_locations, plot_passes, shot_locations, plot_shots

events = load_events(match_names[selected_match])

fig = plot_passes(pass_locations(events)[0], pass_locations(events)[1])

st.pyplot(fig)

fig = plot_shots(shot_locations(events)[0], shot_locations(events)[1])

st.pyplot(fig)

