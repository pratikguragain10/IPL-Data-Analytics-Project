"""This script calculates and plots the extra runs conceded per IPL team in the 2016 season."""

import os
import csv
import matplotlib.pyplot as plt

MATCH_ID = 'match_id'
SEASON = 'season'
BOWLING_TEAM = 'bowling_team'
EXTRA_RUNS = 'extra_runs'


def calculate_extra_runs(deliveries_folder, matches_folder):
    """Calculate total extra runs conceded by each team during IPL 2016."""
    match_ids_2016 = set()
    for file_name in os.listdir(matches_folder):
        if file_name.endswith('.csv'):
            with open(os.path.join(matches_folder, file_name), 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for match in reader:
                    if match[SEASON] == '2016':
                        match_ids_2016.add(match['id'])

    extras_per_team = {}
    for file_name in os.listdir(deliveries_folder):
        if file_name.endswith('.csv'):
            with open(os.path.join(deliveries_folder, file_name), 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for delivery in reader:
                    if delivery[MATCH_ID] in match_ids_2016:
                        team = delivery[BOWLING_TEAM]
                        extras = int(delivery[EXTRA_RUNS])
                        extras_per_team[team] = extras_per_team.get(team, 0) + extras
    return extras_per_team


def plot_extra_runs(extras_per_team):
    """Plot a bar chart showing the extra runs conceded per IPL team."""
    teams = list(extras_per_team.keys())
    extras = list(extras_per_team.values())

    plt.figure(figsize=(7, 5))
    plt.bar(teams, extras, color='orange')
    plt.title('Extra Runs Conceded per Team (IPL 2016)')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/extra-run-conceded-per-team-plot.png')
    plt.show()


def execute():
    """Execute the data processing and plotting pipeline."""
    deliveries_folder = '../sliced-data/sliced_deliveries'
    matches_folder = '../sliced-data/sliced_matches'

    extras_per_team = calculate_extra_runs(deliveries_folder, matches_folder)
    plot_extra_runs(extras_per_team)


if __name__ == "__main__":
    execute()
