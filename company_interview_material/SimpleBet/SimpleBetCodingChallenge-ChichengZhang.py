
# coding: utf-8


import requests
import pandas as pd
import numpy as np


# Grab from URL https://stats.nba.com/stats/commonallplayers? \
# LeagueId=00&Season=2016-17&IsOnlyCurrentSeason=0

#user-agent header
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/71.0.3578.98 Safari/537.36'}

r = requests.get('https://stats.nba.com/stats/commonallplayers?'
                 'LeagueId=00&Season=2016-17&IsOnlyCurrentSeason=0', headers = headers)

# Process Raw Data
rawData = r.text.replace('null', '0')

FatherDict = eval(rawData)
resultSets = str(FatherDict["resultSets"])
resultSets = resultSets[1:-1]
resultSetsDict = eval(resultSets)

PlayerData = pd.DataFrame(resultSetsDict["rowSet"])
PlayerData = PlayerData[[0,1]]
PlayerData.columns = ["player_id", "name"]

# Pick 500 players to do clustering
PlayerData = PlayerData[:500]


# Define a function to combine player's career data in different games
# RegularSeason, PostSeason, AllStarSeason, CollegeSeason


def combine(a, b ,c, d):
    e = []
    if a == []:
        a = np.zeros(21)
    else:
        a = a[0][3:]
    if b == []:
        b = np.zeros(21)
    else:
        b = b[0][3:]
    if c == []:
        c = np.zeros(21)
    else:
        c = c[0][3:]
    if d == []:
        d = np.zeros(21)
    else:
        d = d[0][3:]
    for i in range(21):
        e.append(a[i] + b[i] + c[i] + d[i])
    return e


# Grab from URL https://stats.nba.com/stats/playercareerstats?PerMode=PerGame&PlayerID=X
# Process Raw Data


TotalSeasonData = []

for id in PlayerData['player_id']:
    
    url = 'https://stats.nba.com/stats/playercareerstats?PerMode=PerGame&PlayerID=' + str(id)
    r = requests.get(url, headers = headers)
    
    # Gather player's carrer data of RegularSeason, PostSeason, AllStarSeason,CollegeSeason
    MainDict = eval(r.text.replace('null', '0'))
    RegularSeasonData = MainDict["resultSets"][1]["rowSet"]
    PostSeasonData = MainDict["resultSets"][3]["rowSet"]
    AllStarSeasonData = MainDict["resultSets"][5]["rowSet"]
    CollegeSeasonData = MainDict["resultSets"][7]["rowSet"]

    # Combine Data
    TotalSeasonData.append(combine(RegularSeasonData,PostSeasonData,
                                   AllStarSeasonData,CollegeSeasonData))

# New dataframe for players' carrer data
CareerData=pd.DataFrame(TotalSeasonData,columns = ['GP', 'GS', 'MIN', 'FGM', 
                                                   'FGA', 'FG_PCT', 'FG3M', 
                                                   'FG3A', 'FG3_PCT', 'FTM', 
                                                   'FTA', 'FT_PCT', 'OREB', 
                                                   'DREB', 'REB', 'AST', 'STL', 
                                                   'BLK', 'TOV', 'PF', 'PTS'])    


# Combine Dataframes
PlayerTotalData = pd.merge(PlayerData, CareerData, how='inner', 
                           on=None, left_on=None, right_on=None, 
                           left_index=True, right_index=True, sort=True, 
                           suffixes=('_x', '_y'), copy=True, indicator=False)

# Split DISPLAY_LAST_COMMA_FIRST into first name and last name
PlayerTotalData["first_name"] = PlayerTotalData["name"] \
                              .map(lambda x:x.split(',')[1])

PlayerTotalData["last_name"] = PlayerTotalData["name"] \
                             .map(lambda x:x.split(',')[0])


# K-means Clustering, divide into 5 clusters


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 5, max_iter = 500)

kmeans.fit(CareerData)

label = kmeans.labels_

PlayerTotalData["Label"] = label


# Output Process


Total_Label=[]

for i in range(5):
    Label_List = PlayerTotalData[PlayerTotalData.Label 
                               == i][["player_id", "first_name", "last_name"]]
    
    Label_List_Modified = str(Label_List.to_dict('records')).replace(": ' ",': "') \
        .replace(": '",': "').replace("',",'",').replace("'}",'"}').replace("'",'')
    
    Total_Label.append(Label_List_Modified)
    
output = (str(pd.DataFrame(Total_Label).T.to_dict('list')) \
       .replace("['", "").replace("]'", ""))

# Get output
print(output)