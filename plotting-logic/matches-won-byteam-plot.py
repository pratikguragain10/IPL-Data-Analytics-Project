import matplotlib.pyplot as plt
import os

def read_data(folderpath):
    data=[]
    for file in os.listdir(folderpath):
        if file.endswith('.csv'): 
            filepath = os.path.join(folderpath, file)
            with open(filepath,'r') as file:
                lines=file.readlines()
                headers=lines[0].strip().split(',')
                for line in lines[1:]:
                    row_value = line.strip().split(',')
                    row_dict={}
                    for i,header in enumerate(headers):
                        row_dict[header]=row_value[i]
                    data.append(row_dict)
    return data

def calculations(data):
    matches_won={}
    for row in data:
        team = row['winner']
        season = int(row['season'])
        if season not in matches_won:
            matches_won[season]={}
        if team in matches_won[season]:
            matches_won[season][team]+=1
        else:
            matches_won[season][team]=1
    return matches_won

def plotting(calculated):
    seasons = sorted(calculated.keys())
    teams = set()
    for season_data in calculated.values():
        for team in season_data.keys():
            teams.add(team)
    teams = sorted(list(teams))

    team_counts = {team: [] for team in teams}
    for season in seasons:
        for team in teams:
            count = calculated[season].get(team, 0)
            team_counts[team].append(count)
            
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
        plt.bar(seasons, team_counts[team], bottom=bottom, label=team, color=color)
        bottom = [bottom[i] + team_counts[team][i] for i in range(len(bottom))]
        
folder = '../sliced-data/sliced_matches'
data = read_data(folder)
calculated = calculations(data)
plotting(calculated)

plt.title('Matches per year')
plt.xlabel('Seasons')
plt.ylabel('Matches Won')
plt.xticks(sorted(calculated.keys()), sorted(calculated.keys()), rotation=45, ha='right')
plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()