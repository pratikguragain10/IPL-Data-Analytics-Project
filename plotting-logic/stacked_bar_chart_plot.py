"""
This script calculates and plots the number of IPL matches played by each team per
season using a stacked bar chart.
"""

import os
import matplotlib.pyplot as plt


def read_data(folder_path):
    """Read CSV files from the given folder and return a list of dictionaries for each row."""
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


def calculate_stacked(data):
    """Calculate the number of matches played by each team per season."""
    calculations = {}
    for row in data:
        team1 = row['team1']
        team2 = row['team2']
        season = int(row['season'])

        if season not in calculations:
            calculations[season] = {}

        for team in [team1, team2]:
            calculations[season][team] = calculations[season].get(team, 0) + 1

    return calculations


def plot_stacked(calculated):
    """Plot a stacked bar chart showing the number of matches played by each team per season."""
    seasons = sorted(calculated.keys())
    teams = sorted({team for season_data in calculated.values() for team in season_data.keys()})
    team_games = {team: [] for team in teams}

    for season in seasons:
        for team in teams:
            count = calculated[season].get(team, 0)
            team_games[team].append(count)

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
        plt.bar(seasons, team_games[team], bottom=bottom, label=team, color=color)
        bottom = [bottom[i] + team_games[team][i] for i in range(len(bottom))]


def execute():
    """Execute the full data processing and plotting pipeline."""
    matches_folder = '../sliced-data/sliced_matches'

    data = read_data(matches_folder)
    calculations = calculate_stacked(data)

    plt.figure(figsize=(12, 6))
    plot_stacked(calculations)

    plt.title('Number of Matches Played by Each Team (By Season)')
    plt.xlabel('Season')
    plt.ylabel('Matches Played')
    plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(sorted(calculations.keys()), sorted(calculations.keys()), rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/stacked-bar-chart-plot.png')
    plt.show()


if __name__ == "__main__":
    execute()
