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

def calcualte_stacked(datas):
    calculations={}
    for row in datas:
        team1 = row['team1']
        team2 = row['team2']
        seasons = int(row['season'])
        if seasons not in calculations:
            calculations[seasons]={}
        for team in [team1,team2]:
            if team in calculations[seasons]:
                calculations[seasons][team1]+=1
            else:
                calculations[seasons][team1]=1
    return calculations


def plotting(calculated):
    seasons = sorted(calculated.keys())
    teams = set()
    for sdata in calculated.values():
        for team in sdata.keys():
            teams.add(team)
            
    teams=sorted(list(teams))
    teams_games = {team : [] for team in teams}
    
    for season in seasons:
        for team in teams:
            count = calculated[season].get(team,0)
            teams_games[team].append(count)  
    
    team_colors = {
    'Chennai Super Kings': '#F1C40F',   # yellow
    'Mumbai Indians': '#1F77B4',        # blue
    'Kolkata Knight Riders': '#6C3483', # purple
    'Royal Challengers Bangalore': '#E74C3C', # red
    'Rajasthan Royals': '#AF7AC5',
    'Sunrisers Hyderabad': '#E67E22',
    'Delhi Daredevils': '#3498DB',
    'Kings XI Punjab': '#C0392B',
    'Deccan Chargers': '#808B96',
    'Gujarat Lions': '#F39C12',
    'Rising Pune Supergiant': '#8E44AD',
    'Rising Pune Supergiants': '#BB8FCE',
    'Pune Warriors': '#16A085',
}
    
    bottom = [0] * len(seasons)
    for team in teams:
        color = team_colors.get(team, None)
        plt.bar(seasons, teams_games[team], bottom=bottom, label=team, color=color)
        bottom = [bottom[i] + teams_games[team][i] for i in range(len(bottom))]      
            
                    
    
    
folder = '../sliced-data/sliced_matches'
data = read_data(folder)
calculation = calcualte_stacked(data) 
plt.figure(figsize=(12,6))
plotting(calculation)

plt.title('Number of Matches Played by Each Team (By Season)')
plt.xlabel('Season')
plt.ylabel('Matches Played')
plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(sorted(calculation.keys()), sorted(calculation.keys()), rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../plotting-images/stacked-bar-chart-plot.png')
plt.show()




