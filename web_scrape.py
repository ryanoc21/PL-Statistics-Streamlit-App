"""
This file contains the class that will perform the web scraping using pandas,
which makes up the majority of the backend functionality of our streamlit web app.
The class contains methods for reading and plotting the data.
"""
import pandas as pd
import plotly.express as px
from datetime import date


class DataProcess:

    def __init__(self, team):
        self.team = team

        # Store each team code in a dictionary
        self.top_score_code = {
            "Arsenal": "18bb7c10/2022-2023/goallogs/c9/Arsenal-Goal-Logs-Premier-League",
            "Manchester City": "b8fd03ef/2022-2023/goallogs/c9/Manchester-City-Goal-Logs-Premier-League",
            "Newcastle Utd": "b2b47a98/2022-2023/goallogs/c9/Newcastle-United-Goal-Logs-Premier-League",
            "Tottenham": "361ca564/2022-2023/goallogs/c9/Tottenham-Hotspur-Goal-Logs-Premier-League",
            "Manchester Utd": "19538871/2022-2023/goallogs/c9/Manchester-United-Goal-Logs-Premier-League",
            "Liverpool": "822bd0ba/2022-2023/goallogs/c9/Liverpool-Goal-Logs-Premier-League",
            "Fulham": "fd962109/2022-2023/goallogs/c9/Fulham-Goal-Logs-Premier-League",
            "Brentford": "cd051869/2022-2023/goallogs/c9/Brentford-Goal-Logs-Premier-League",
            "Brighton": "d07537b9/2022-2023/goallogs/c9/Brighton-and-Hove-Albion-Goal-Logs-Premier-League",
            "Chelsea": "cff3d9bb/2022-2023/goallogs/c9/Chelsea-Goal-Logs-Premier-League",
            "Aston Villa": "8602292d/2022-2023/goallogs/c9/Aston-Villa-Goal-Logs-Premier-League",
            "Crystal Palace": "47c64c55/2022-2023/goallogs/c9/Crystal-Palace-Goal-Logs-Premier-League",
            "Nottingham Forest": "e4a775cb/2022-2023/goallogs/c9/Nottingham-Forest-Goal-Logs-Premier-League",
            "Leicester City": "a2d435b3/2022-2023/goallogs/c9/Leicester-City-Goal-Logs-Premier-League",
            "Leeds Utd": "5bfb9659/2022-2023/goallogs/c9/Leeds-United-Goal-Logs-Premier-League",
            "West Ham": "7c21e445/2022-2023/goallogs/c9/West-Ham-United-Goal-Logs-Premier-League",
            "Wolves": "8cec06e1/2022-2023/goallogs/c9/Wolverhampton-Wanderers-Goal-Logs-Premier-League",
            "Bournemouth": "4ba7cbea/2022-2023/goallogs/c9/Bournemouth-Goal-Logs-Premier-League",
            "Everton": "d3fd31cc/2022-2023/goallogs/c9/Everton-Goal-Logs-Premier-League",
            "Southampton": "33c895d4/2022-2023/goallogs/c9/Southampton-Goal-Logs-Premier-League"
        }

        # Url for the top scorers
        self.top_score_url = f"https://fbref.com/en/squads/{self.top_score_code.get(team)}"

        # Read top_score_url to a dataframe
        self.df = pd.read_html(self.top_score_url)
        self.df_for = self.df[0]

    def plot_scorer(self):
        # Get a bar chart of the top scorer
        score = self.df_for['Scorer'].value_counts()
        df_top_scorer = pd.DataFrame({'Name': score.index, 'GoalsNo': score.values})
        # return df_top_scorer

        fig_bar = px.bar(df_top_scorer, x='Name', y='GoalsNo',
                         title=f"Top Scorers as of {date.today()}",
                         labels={
                             'GoalsNo': 'Number of Goals',
                             'Name': 'Player'
                         })
        return fig_bar