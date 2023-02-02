"""
This file contains the code for the frontend streamlit web data app.
"""

import streamlit as st
from web_scrape import DataProcess

# Create the interactive elements for the app
st.title("Premier League Team Top Scorer Stats ⚽️")
st.write("""
This web app uses python to scrape data about premier league teams. The user can input their chosen team 
and data about the top scorers will be displayed back to them. Data are read using the pandas read html method 
and the plots are produced using plotly. All data are taken from https://fbref.com/en/. 
""")
team = st.selectbox("Pick a team",
                    ("Arsenal", "Liverpool", "Manchester City", "Manchester Utd",
                     "Newcastle Utd", "Tottenham", "Brighton", "Fulham", "Brentford",
                     "Chelsea", "Aston Villa", "Crystal Palace", "Nottingham Forest",
                     "Leicester City", "Leeds Utd", "West Ham", "Wolves",
                     "Bournemouth", "Everton", "Southampton"))

st.subheader(f"Top Scorers for {team}")

if team:
    team_data = DataProcess(team)
    st.plotly_chart(team_data.plot_scorer())