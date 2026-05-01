import streamlit as st
from analysis import load_competitions


st.title("FOOTBALL STATISTICS")

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

