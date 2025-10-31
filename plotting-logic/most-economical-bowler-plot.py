import matplotlib.pyplot as plt
import os

def read_data(folderpath):
    data=[]
    for file in os.listdir(folderpath):
        if file.endswith('.csv'): 
            filepath = os.path.join(folderpath, file)
            with open(filepath,'r') as f:
                lines=f.readlines()
                headers=lines[0].strip().split(',')
                for line in lines[1:]:
                    values=line.strip().split(',')
                    row={}
                    for i,header in enumerate(headers):
                        row[header]=values[i]
                    data.append(row)
    return data


def top_economical_bowlers(deliveries, matches):
    match_2015_ids = []
    for m in matches:
        if m['season'] == '2015':
            match_2015_ids.append(m['id'])
    bowler_stats = {}
    for d in deliveries:
        if d['match_id'] in match_2015_ids:
            bowler = d['bowler']
            total_runs = int(d['total_runs'])
            noball = int(d['noball_runs'])
            wide = int(d['wide_runs'])
            legal_ball = 1 if (noball == 0 and wide == 0) else 0

            if bowler not in bowler_stats:
                bowler_stats[bowler] = {'runs':0, 'balls':0}

            bowler_stats[bowler]['runs'] += total_runs
            bowler_stats[bowler]['balls'] += legal_ball
    economy = {}
    for bowler, stats in bowler_stats.items():
        if stats['balls'] > 0:
            overs = stats['balls'] / 6
            eco = stats['runs'] / overs
            economy[bowler] = round(eco, 2)
    sorted_bowlers = sorted(economy.items(), key=lambda x: x[1])[:10]
    return sorted_bowlers

folder_matches = '../sliced-data/sliced_matches'
folder_deliveries = '../sliced-data/sliced_deliveries'

matches = read_data(folder_matches)
deliveries = read_data(folder_deliveries)

top10 = top_economical_bowlers(deliveries, matches)

bowlers = [b[0] for b in top10]
economy = [b[1] for b in top10]

plt.figure(figsize=(10,5))
plt.bar(bowlers, economy, color='orange')
plt.title('Top 10 Economical Bowlers in IPL 2015')
plt.xlabel('Bowler')
plt.ylabel('Economy Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
