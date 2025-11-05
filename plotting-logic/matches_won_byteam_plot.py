"""This script calculates and plots the number of IPL matches won by each team per season."""

import os
import matplotlib.pyplot as plt

def read_data(folder_path):
    """Read CSV files from the given folder and return a list of row dictionaries."""
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    row_values = line.strip().split(',')
                    row_dict = {header: row_values[i] for i, header in enumerate(headers)}
                    data.append(row_dict)
    return data


def calculate_matches_won(data):
    """Calculate the number of matches won by each IPL team per season."""
    matches_won = {}
    for match in data:
        team = match['winner']
        season = int(match['season'])
        if season not in matches_won:
            matches_won[season] = {}
        matches_won[season][team] = matches_won[season].get(team, 0) + 1
    return matches_won


def plot_matches_won(matches_won):
    """Plot a stacked bar chart showing matches won by teams across seasons."""
    seasons = sorted(matches_won.keys())
    teams = sorted({team for season_data in matches_won.values() for team in season_data.keys()})

    team_counts = {team: [] for team in teams}
    for season in seasons:
        for team in teams:
            count = matches_won[season].get(team, 0)
            team_counts[team].append(count)

    team_colors = {
        'Chennai Super Kings': '#F1C40F',
        'Mumbai Indians': '#1F77B4',
        'Kolkata Knight Riders': '#6C3483',
        'Royal Challengers Bangalore': '#E74C3C',
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

    plt.title('Matches Won by IPL Teams per Season')
    plt.xlabel('Seasons')
    plt.ylabel('Matches Won')
    plt.xticks(seasons, seasons, rotation=45, ha='right')
    plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('../plotting-images/matches-won-by-team-plot.png')
    plt.show()


def execute():
    """Execute the full data reading, calculation, and plotting pipeline."""
    folder = '../sliced-data/sliced_matches'
    data = read_data(folder)
    matches_won = calculate_matches_won(data)
    plot_matches_won(matches_won)


if __name__ == "__main__":
    execute()
