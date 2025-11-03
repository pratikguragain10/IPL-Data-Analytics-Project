import pandas as pd
import matplotlib.pyplot as plt
import os

def read_data(folderpath):
    datas=[]
    for files in os.listdir(folderpath):
        if files.endswith('.csv'):
            filepath=os.path.join(folderpath,files)
            with open (filepath,'r') as files:
                lines=files.readlines()
                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    row_values = line.strip().split(',')
                    row_dict={}
                    for i,header in enumerate(headers):
                        row_dict[header]=row_values[i]
                    datas.append(row_dict)
    return datas

def calculate(deliveries, matches):
    match_ids_2016 = []
    for row in matches:
        if row['season'] == '2016':
            match_ids_2016.append(row['id'])
    extras_per_team = {}
    for row in deliveries:
        if row['match_id'] in match_ids_2016:
            team = row['bowling_team']
            extras = int(row['extra_runs'])
            if team in extras_per_team:
                extras_per_team[team] += extras
            else:
                extras_per_team[team] = extras
    return extras_per_team

deliveries = read_data('../sliced-data/sliced_deliveries')
matches = read_data('../sliced-data/sliced_matches')
    
folder = '../sliced-data/sliced_deliveries'
data = read_data(folder)
calculation = calculate(deliveries,matches)

team = list(calculation.keys())
extras = list(calculation.values())


plt.figure(figsize=(7, 5))
plt.bar(team, extras, color='orange')
plt.title('Extra runs per team')
plt.xlabel('Teams')
plt.ylabel('Extra Run')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../plotting-images/extra-run-conceded-per-team-plot.png')
plt.show()
