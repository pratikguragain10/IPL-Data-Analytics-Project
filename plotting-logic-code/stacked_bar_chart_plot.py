"""
Optimized script to calculate and plot the number of IPL matches played by each team per season.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

SEASON = 'season'
TEAM1 = 'team1'
TEAM2 = 'team2'


def load_matches(matches_file):
    """
    Reads the matches CSV and returns a list of rows as dictionaries.
    Only necessary columns are processed.
    """
    matches = []
    with open(matches_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            matches.append({
                SEASON: int(row[SEASON]),
                TEAM1: row[TEAM1],
                TEAM2: row[TEAM2],
            })
    return matches


def calculate_matches_played(matches):
    """
    Calculate the number of matches played by each team per season.
    Returns a nested dictionary: {season: {team: matches_played}}
    """
    matches_played = {}
    for match in matches:
        season = match[SEASON]
        team1 = match[TEAM1]
        team2 = match[TEAM2]

        if season not in matches_played:
            matches_played[season] = {}

        for team in [team1, team2]:
            matches_played[season][team] = matches_played[season].get(team, 0) + 1

    return matches_played


def plot_matches_played(matches_played):
    """Plot a stacked bar chart showing matches played by each team per season."""
    seasons = sorted(matches_played.keys())
    teams = sorted({team for season_data in matches_played.values() for team in season_data.keys()})
    team_counts = {team: [] for team in teams}

    for season in seasons:
        for team in teams:
            team_counts[team].append(matches_played[season].get(team, 0))

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
        color = team_colors.get(team)
        plt.bar(seasons, team_counts[team], bottom=bottom, label=team, color=color)
        bottom = [bottom[i] + team_counts[team][i] for i in range(len(bottom))]


def execute(matches_file):
    """Execute the full data processing and plotting pipeline."""
    matches = load_matches(matches_file)
    matches_played = calculate_matches_played(matches)

    plt.figure(figsize=(12, 6))
    plot_matches_played(matches_played)

    plt.title(
        'Number of Matches Played by Each Team (By Season)'
    )
    plt.xlabel('Season')
    plt.ylabel('Matches Played')
    plt.legend(
        title='Teams',
        bbox_to_anchor=(1.05, 1),
        loc='upper left'
    )
    plt.xticks(
        sorted(matches_played.keys()),
        sorted(matches_played.keys()),
        rotation=45,
        ha='right'
    )
    plt.tight_layout()
    plt.savefig('../plotting-images/stacked-bar-chart-plot.png')
    plt.show()


if __name__ == "__main__":
    MATCHES_PATH = '../data/matches.csv'
    execute(MATCHES_PATH)
