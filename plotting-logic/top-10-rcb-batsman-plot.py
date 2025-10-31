import matplotlib.pyplot as plt
import os

def read_data(folderpath):
    data=[]
    for files in os.listdir(folderpath):
        if files.endswith('.csv'):
            filepath = os.path.join(folderpath,files)
            with open(filepath,'r') as file:
                lines = file.readlines()
                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    row_values = line.strip().split(',')
                    row_dict = {}
                    for i,header in enumerate(headers):
                        row_dict[header]=row_values[i]
                    data.append(row_dict)
    return data

def top_10(data):
    datas={}
    for row in data:
        if row['batting_team'] == 'Royal Challengers Bangalore':
            batsmen = row['batsman']
            runs = int(row['batsman_runs'])
            if batsmen in datas:
                datas[batsmen]+=runs
            else:
                datas[batsmen]=runs
            
    items=[]
    for batsmen ,run in (datas.items()):
        items.append((run,batsmen))
    items = sorted(items, reverse=True)
    top10 = items[:10]

    top10_dict ={}
    for runs,batsman in top10:
        top10_dict[batsman]=runs
    return top10_dict
        

folder='../sliced-data/sliced_deliveries'
data = read_data(folder)
batsmen = top_10(data)

batter = list(batsmen.keys())
runs = list(batsmen.values())

plt.figure(figsize=(10, 5))
plt.bar(batter, runs, color='skyblue')
plt.title('Top 10 Run Scorers for Royal Challengers Bangalore (All Seasons)')
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.xticks(rotation=45, ha='right')   
plt.tight_layout()  
plt.show()
