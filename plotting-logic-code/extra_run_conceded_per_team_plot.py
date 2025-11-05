"""
Optimized script to calculate and plot extra runs conceded per IPL team in 2016.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

MATCH_ID = 'match_id'
SEASON = 'season'
BOWLING_TEAM = 'bowling_team'
EXTRA_RUNS = 'extra_runs'


def load_match_seasons(matches_file):
    """
    Reads match file and returns a dictionary mapping match_id to season.
    Only store necessary info to reduce memory usage.
    """
    match_season_map = {}
    with open(matches_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for match in reader:
            match_season_map[match['id']] = match[SEASON]
    return match_season_map


def calculate_extra_runs(deliveries_file, match_season_map, target_season='2016'):
    """Calculate total extra runs conceded per team for a given season."""
    extras_per_team = {}

    with open(deliveries_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for delivery in reader:
            match_id = delivery[MATCH_ID]
            # Skip deliveries not in the target season
            if match_season_map.get(match_id) != target_season:
                continue

            team = delivery[BOWLING_TEAM]
            extras = int(delivery[EXTRA_RUNS])
            extras_per_team[team] = extras_per_team.get(team, 0) + extras

    return extras_per_team


def plot_extra_runs(extras_per_team):
    """Plot a bar chart showing extra runs conceded per IPL team."""
    teams = list(extras_per_team.keys())
    extras = list(extras_per_team.values())

    plt.figure(figsize=(8, 5))
    plt.bar(teams, extras, color='orange', edgecolor='black')
    plt.title('Extra Runs Conceded per Team (IPL 2016)')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/extra-run-conceded-per-team-plot.png')
    plt.show()


def execute(matches_file, deliveries_file):
    """Execute the data processing and plotting pipeline."""
    match_season_map = load_match_seasons(matches_file)
    extras_per_team = calculate_extra_runs(deliveries_file, match_season_map)
    plot_extra_runs(extras_per_team)

if __name__ == "__main__":
    MATCHES_PATH = '../data/matches.csv'
    DELIVERIES_PATH = '../data/deliveries.csv'

    execute(MATCHES_PATH, DELIVERIES_PATH)
