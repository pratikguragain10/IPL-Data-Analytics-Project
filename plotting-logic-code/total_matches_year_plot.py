"""
Optimized script to calculate and plot the total number of IPL matches
played per season as a bar chart.
Uses minimal memory and no `os` module.
"""

import csv
import matplotlib.pyplot as plt

SEASON = 'season'


def load_matches(matches_file):
    """
    Reads the matches CSV and returns a list of rows as dictionaries.
    Only necessary columns are processed.
    """
    matches = []
    with open(matches_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            matches.append({SEASON: int(row[SEASON])})
    return matches


def calculate_matches_per_season(matches):
    """Calculate the total number of matches played per season."""
    total_matches = {}
    for match in matches:
        season = match[SEASON]
        total_matches[season] = total_matches.get(season, 0) + 1
    return total_matches


def plot_matches_per_season(total_matches):
    """Plot a bar chart showing total matches played per season."""
    seasons = sorted(total_matches.keys())
    match_counts = [total_matches[s] for s in seasons]

    plt.figure(figsize=(10, 5))
    plt.bar(seasons, match_counts, color='violet', edgecolor='black')
    plt.title('Total Matches Played Per Season')
    plt.xlabel('Season')
    plt.ylabel('Matches')
    plt.xticks(seasons, rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/total-matches-year-plot.png')
    plt.show()


def execute(matches_file):
    """Execute the data processing and plotting pipeline."""
    matches = load_matches(matches_file)
    total_matches = calculate_matches_per_season(matches)
    plot_matches_per_season(total_matches)


if __name__ == "__main__":
    MATCHES_PATH = '../data/matches.csv'
    execute(MATCHES_PATH)
