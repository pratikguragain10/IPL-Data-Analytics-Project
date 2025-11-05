"""
This script reads IPL delivery data and plots the top 10 run scorers
for Royal Challengers Bangalore across all seasons.
"""

import os
import matplotlib.pyplot as plt


def read_data(folder_path):
    """Read all CSV files in the given folder and return a list of row dictionaries."""
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    values = line.strip().split(',')
                    row_dict = {header: values[i] for i, header in enumerate(headers)}
                    data.append(row_dict)
    return data


def calculate_top_10_batsmen(data):
    """Return a dictionary of the top 10 run scorers for Royal Challengers Bangalore."""
    batsman_runs = {}
    for row in data:
        if row['batting_team'] == 'Royal Challengers Bangalore':
            batsman = row['batsman']
            runs = int(row['batsman_runs'])
            batsman_runs[batsman] = batsman_runs.get(batsman, 0) + runs

    sorted_batsmen = sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True)
    top_10 = dict(sorted_batsmen[:10])
    return top_10


def execute():
    """Execute the data reading, calculation, and plotting pipeline."""
    folder = '../sliced-data/sliced_deliveries'
    data = read_data(folder)
    top_batsmen = calculate_top_10_batsmen(data)

    batters = list(top_batsmen.keys())
    runs = list(top_batsmen.values())

    plt.figure(figsize=(10, 5))
    plt.bar(batters, runs, color='skyblue')
    plt.title('Top 10 Run Scorers for Royal Challengers Bangalore (All Seasons)')
    plt.xlabel('Batsman')
    plt.ylabel('Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/top-10-rcb-batsman-plot.png')
    plt.show()


if __name__ == "__main__":
    execute()
