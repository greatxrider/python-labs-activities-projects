#This program uses NBA API to determine the points of a Team, won or lost
import pandas as pd
from nba_api.stats.static import teams
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import leaguegamefinder
import requests


def one_dict(list_dict):
    allkeys_of_list_dict=list_dict[0].keys()
    
    #dictionaries with keys only and no values.
    out_dict={key:[] for key in allkeys_of_list_dict} 
     
    for dict_ in list_dict:
        for key, value in dict_.items(): #put all values of list_dict to the out_dict, to each keys.
            out_dict[key].append(value)
    return out_dict    

nba_teams = teams.get_teams()
Z = nba_teams[0:3]
print(Z)

dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
print(df_teams.head())

df_warriors = df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors = df_warriors[['id']].values[0][0]
print(id_warriors)

#accessing the Golden_State.pkl file
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head())

games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(['away','home'])
plt.show()