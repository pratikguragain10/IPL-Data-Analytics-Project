"""This script calculates and plots the top 10 most economical bowlers in the IPL 2015 season."""

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
                    values = line.strip().split(',')
                    row_dict = {header: values[i] for i, header in enumerate(headers)}
                    data.append(row_dict)
    return data


def calculate_top_economical_bowlers(deliveries, matches):
    """Calculate and return the top 10 most economical bowlers for IPL 2015."""
    match_ids_2015 = {match['id'] for match in matches if match['season'] == '2015'}

    bowler_stats = {}
    for delivery in deliveries:
        if delivery['match_id'] in match_ids_2015:
            bowler = delivery['bowler']
            total_runs = int(delivery['total_runs'])
            no_ball = int(delivery['noball_runs'])
            wide = int(delivery['wide_runs'])
            is_legal = 1 if (no_ball == 0 and wide == 0) else 0

            if bowler not in bowler_stats:
                bowler_stats[bowler] = {'runs': 0, 'balls': 0}

            bowler_stats[bowler]['runs'] += total_runs
            bowler_stats[bowler]['balls'] += is_legal

    economy = {}
    for bowler, stats in bowler_stats.items():
        if stats['balls'] > 0:
            overs = stats['balls'] / 6
            economy_rate = stats['runs'] / overs
            economy[bowler] = round(economy_rate, 2)

    sorted_bowlers = sorted(economy.items(), key=lambda item: item[1])[:10]
    return sorted_bowlers

def plot_top_bowlers(sorted_bowlers):
    """Plot a bar chart of the top 10 most economical bowlers in IPL 2015."""
    bowlers = [bowler for bowler, _ in sorted_bowlers]
    economy_rates = [eco for _, eco in sorted_bowlers]

    plt.figure(figsize=(10, 5))
    plt.bar(bowlers, economy_rates, color='orange')
    plt.title('Top 10 Economical Bowlers in IPL 2015')
    plt.xlabel('Bowler')
    plt.ylabel('Economy Rate')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../plotting-images/most-economical-bowler-plot.png')
    plt.show()
                 
def execute():
    """Execute the data reading, calculation, and plotting pipeline."""
    matches_folder = '../sliced-data/sliced_matches'
    deliveries_folder = '../sliced-data/sliced_deliveries'

    matches = read_data(matches_folder)
    deliveries = read_data(deliveries_folder)

    top_bowlers = calculate_top_economical_bowlers(deliveries, matches)
    plot_top_bowlers(top_bowlers)

if __name__ == "__main__":
    execute()
