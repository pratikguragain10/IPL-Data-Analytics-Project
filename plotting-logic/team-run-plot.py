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


def calculate_run(data):
    total_team_run={}
    for row in data:
        team = row['batting_team']
        run = int(row['total_runs'])
        if team in total_team_run:
            total_team_run[team]+=run
        else:
            total_team_run[team]=run
    return total_team_run

path = '../sliced-data/sliced_deliveries'
data = read_data(path)
team_run = calculate_run(data)

teams = list(team_run.keys())
runs = list(team_run.values())

plt.figure(figsize=(10, 5))
plt.bar(teams, runs, color='skyblue')
plt.title('Total runs scored by teams')
plt.xlabel('Team')
plt.ylabel('Runs')
plt.xticks(rotation=45, ha='right')   
plt.tight_layout()  
plt.show()
