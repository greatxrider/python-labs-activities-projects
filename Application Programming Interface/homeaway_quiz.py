# Calculate the mean for the column PTS for the 
# dataframes games_home and  games_away:

import nba_test as nba

Z = nba.games_home['PTS'].mean()
X = nba.games_away['PTS'].mean()
print(X)
print(Z)