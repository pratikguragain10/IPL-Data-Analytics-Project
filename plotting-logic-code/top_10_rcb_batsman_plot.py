"""
Optimized script to calculate and plot the top 10 run scorers
for Royal Challengers Bangalore across all IPL seasons.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

TEAM = 'batting_team'
BATSMAN = 'batsman'
RUNS = 'batsman_runs'
TARGET_TEAM = 'Royal Challengers Bangalore'


def load_deliveries(deliveries_file):
    """
    Reads the deliveries CSV and returns a list of rows as dictionaries.
    Only necessary columns are processed.
    """
    deliveries = []
    with open(deliveries_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[TEAM] == TARGET_TEAM:
                deliveries.append({
                    BATSMAN: row[BATSMAN],
                    RUNS: int(row[RUNS]),
                })
    return deliveries


def calculate_top_10_batsmen(deliveries):
    """Return the top 10 run scorers for Royal Challengers Bangalore."""
    batsman_runs = {}
    for delivery in deliveries:
        batsman = delivery[BATSMAN]
        batsman_runs[batsman] = batsman_runs.get(batsman, 0) + delivery[RUNS]

    # Sort and take top 10
    sorted_batsmen = sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True)
    top_10 = dict(sorted_batsmen[:10])
    return top_10


def plot_top_batsmen(top_batsmen):
    """Plot a bar chart of the top 10 RCB run scorers."""
    batters = list(top_batsmen.keys())
    runs = list(top_batsmen.values())

    plt.figure(figsize=(10, 5))
    plt.bar(batters, runs, color='skyblue', edgecolor='black')
    plt.title('Top 10 Run Scorers for Royal Challengers Bangalore (All Seasons)')
    plt.xlabel('Batsman')
    plt.ylabel('Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/top-10-rcb-batsman-plot.png')
    plt.show()


def execute(deliveries_file):
    """Execute the full data processing and plotting pipeline."""
    deliveries = load_deliveries(deliveries_file)
    top_batsmen = calculate_top_10_batsmen(deliveries)
    plot_top_batsmen(top_batsmen)


if __name__ == "__main__":
    DELIVERIES_PATH = '../data/deliveries.csv'
    execute(DELIVERIES_PATH)
