"""
Optimized script to calculate and plot the total runs scored by each IPL team.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

TEAM = 'batting_team'
RUNS = 'total_runs'


def load_deliveries(deliveries_file):
    """
    Reads the deliveries CSV and returns a list of rows as dictionaries.
    Only necessary columns are processed.
    """
    deliveries = []
    with open(deliveries_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            deliveries.append({
                TEAM: row[TEAM],
                RUNS: int(row[RUNS]),
            })
    return deliveries


def calculate_team_runs(deliveries):
    """Calculate total runs scored by each team."""
    total_team_runs = {}
    for delivery in deliveries:
        team = delivery[TEAM]
        total_team_runs[team] = total_team_runs.get(team, 0) + delivery[RUNS]
    return total_team_runs


def plot_team_runs(total_team_runs):
    """Plot a bar chart showing total runs scored by each IPL team."""
    teams = list(total_team_runs.keys())
    runs = list(total_team_runs.values())

    plt.figure(figsize=(10, 5))
    plt.bar(teams, runs, color='skyblue', edgecolor='black')
    plt.title('Total Runs Scored by Teams')
    plt.xlabel('Team')
    plt.ylabel('Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/team-run-plot.png')
    plt.show()


def execute(deliveries_file):
    """Execute the full data processing and plotting pipeline."""
    deliveries = load_deliveries(deliveries_file)
    total_team_runs = calculate_team_runs(deliveries)
    plot_team_runs(total_team_runs)


if __name__ == "__main__":
    DELIVERIES_PATH = '../data/deliveries.csv'
    execute(DELIVERIES_PATH)
