"""
Optimized script to calculate and plot the top 10 most economical bowlers in IPL 2015.
Uses minimal memory and filters bowlers with at least 12 legal deliveries.
"""

import csv
import matplotlib.pyplot as plt

MATCH_ID = 'match_id'
SEASON = 'season'
BOWLER = 'bowler'
TOTAL_RUNS = 'total_runs'
NOBALL_RUNS = 'noball_runs'
WIDE_RUNS = 'wide_runs'


def load_match_ids(matches_file, target_season='2015'):
    """Return a set of match IDs for the target season."""
    match_ids = set()
    with open(matches_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for match in reader:
            if match[SEASON] == target_season:
                match_ids.add(match['id'])
    return match_ids


def calculate_top_economical_bowlers(deliveries_file, match_ids, min_legal_balls=12):
    """Calculate top 10 economical bowlers who bowled at least `min_legal_balls`."""
    bowler_stats = {}

    with open(deliveries_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for delivery in reader:
            if delivery[MATCH_ID] not in match_ids:
                continue

            bowler = delivery[BOWLER]
            total_runs = int(delivery[TOTAL_RUNS])
            no_ball = int(delivery[NOBALL_RUNS])
            wide = int(delivery[WIDE_RUNS])
            is_legal = 1 if (no_ball == 0 and wide == 0) else 0

            if bowler not in bowler_stats:
                bowler_stats[bowler] = {'runs': 0, 'balls': 0}

            bowler_stats[bowler]['runs'] += total_runs
            bowler_stats[bowler]['balls'] += is_legal

    # Filter bowlers who bowled at least min_legal_balls
    filtered_bowlers = {b: s for b, s in bowler_stats.items() if s['balls'] >= min_legal_balls}

    # Calculate economy (per 6-ball over)
    economy = {b: round(s['runs'] / (s['balls'] / 6), 2) for b, s in filtered_bowlers.items()}

    # Top 10 economical bowlers
    sorted_bowlers = sorted(economy.items(), key=lambda x: x[1])[:10]
    return sorted_bowlers


def plot_top_bowlers(sorted_bowlers):
    """Plot bar chart for top 10 economical bowlers."""
    bowlers = [b for b, _ in sorted_bowlers]
    economy_rates = [e for _, e in sorted_bowlers]

    plt.figure(figsize=(10, 5))
    plt.bar(bowlers, economy_rates, color='orange', edgecolor='black')
    plt.title('Top 10 Economical Bowlers in IPL 2015 (Min 12 Balls)')
    plt.xlabel('Bowler')
    plt.ylabel('Economy Rate')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/most-economical-bowler-plot.png')
    plt.show()


def execute(matches_file, deliveries_file):
    """Run the full pipeline."""
    match_ids = load_match_ids(matches_file)
    top_bowlers = calculate_top_economical_bowlers(deliveries_file, match_ids)
    plot_top_bowlers(top_bowlers)


if __name__ == "__main__":
    MATCHES_PATH = '../data/matches.csv'
    DELIVERIES_PATH = '../data/deliveries.csv'

    execute(MATCHES_PATH, DELIVERIES_PATH)
