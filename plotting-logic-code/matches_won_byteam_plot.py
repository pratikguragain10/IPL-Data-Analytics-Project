"""
Optimized script to calculate and plot the number of IPL matches won by each team per season.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

SEASON = 'season'
WINNER = 'winner'


def load_matches(matches_file):
    """
    Reads matches CSV and returns a nested dictionary mapping season -> team -> matches won.
    Only stores necessary info to reduce memory usage.
    """
    matches_won = {}

    with open(matches_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for match in reader:
            season = int(match[SEASON])
            team = match[WINNER].strip()
            if not team:  
                continue

            if season not in matches_won:
                matches_won[season] = {}

            matches_won[season][team] = matches_won[season].get(team, 0) + 1

    return matches_won


def plot_matches_won(matches_won):
    """Plot a stacked bar chart showing matches won by IPL teams across seasons."""
    seasons = sorted(matches_won.keys())
    teams = sorted({team for season_data in matches_won.values() for team in season_data.keys()})

    team_counts = {team: [] for team in teams}
    for season in seasons:
        for team in teams:
            team_counts[team].append(matches_won[season].get(team, 0))

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
    plt.figure(figsize=(10, 6))
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


def execute(matches_file):
    """Execute the full data processing and plotting pipeline."""
    matches_won = load_matches(matches_file)
    plot_matches_won(matches_won)


if __name__ == "__main__":
    MATCHES_PATH = '../data/matches.csv'
    execute(MATCHES_PATH)
