"""
This script reads IPL delivery data from sliced CSV files and plots
the total runs scored by each team using a bar chart.
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


def calculate_runs(data):
    """Calculate total runs scored by each team."""
    total_team_runs = {}
    for row in data:
        team = row['batting_team']
        runs = int(row['total_runs'])
        total_team_runs[team] = total_team_runs.get(team, 0) + runs
    return total_team_runs


def execute():
    """Execute the data reading, calculation, and plotting pipeline."""
    path = '../sliced-data/sliced_deliveries'
    data = read_data(path)
    team_runs = calculate_runs(data)

    teams = list(team_runs.keys())
    runs = list(team_runs.values())

    plt.figure(figsize=(10, 5))
    plt.bar(teams, runs, color='skyblue')
    plt.title('Total Runs Scored by Teams')
    plt.xlabel('Team')
    plt.ylabel('Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/team-run-plot.png')
    plt.show()


if __name__ == "__main__":
    execute()
