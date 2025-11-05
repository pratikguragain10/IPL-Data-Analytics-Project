"""
This script reads IPL match data and plots the total number of matches
played per season as a bar chart.
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


def calculate_matches_per_season(data):
    """Calculate and return the total number of matches played per season."""
    total_matches = {}
    for row in data:
        season = int(row['season'])
        total_matches[season] = total_matches.get(season, 0) + 1
    return total_matches


def execute():
    """Execute the data reading, calculation, and plotting pipeline."""
    folder = '../sliced-data/sliced_matches'
    data = read_data(folder)
    matches = calculate_matches_per_season(data)

    seasons = sorted(matches.keys())
    match_counts = [matches[s] for s in seasons]

    plt.figure(figsize=(10, 5))
    plt.bar(seasons, match_counts, color='violet')

    plt.title('Total Matches Played Per Season')
    plt.xlabel('Season')
    plt.ylabel('Matches')
    plt.xticks(seasons, rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/total-matches-year-plot.png')
    plt.show()


if __name__ == "__main__":
    execute()
