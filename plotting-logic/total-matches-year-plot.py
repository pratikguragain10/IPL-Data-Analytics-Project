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

def calculations(data):
    total_matches={}
    for row in data:
        seasons=int(row['season'])
        id = int(row['id'])
        if seasons in total_matches:
            total_matches[seasons]+=1
        else:
            total_matches[seasons]=1
    return total_matches
            
            
path = '../sliced-data/sliced_matches'
data = read_data(path)
matches = calculations(data)

seasons = sorted(matches.keys())
match_counts = [matches[s] for s in seasons]

plt.figure(figsize=(10, 5))
plt.bar(seasons, match_counts, color='violet')

plt.title('Matches per year')
plt.xlabel('Season')
plt.ylabel('Matches')
plt.xticks(seasons, rotation=45, ha='right')
plt.tight_layout()
plt.show()