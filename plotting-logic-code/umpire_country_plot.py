"""
Plot number of foreign umpires by country using only umpire_countries.csv.
No pandas used.
"""

import csv
import matplotlib.pyplot as plt


def read_umpire_countries(mapping_path):
    """Read umpire-country mappings and count non-Indian umpires by country."""
    country_count = {}
    with open(mapping_path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            umpire = row.get("umpire", "").strip()
            country = row.get("country", "").strip()
            if not umpire or not country or country.lower() == "india":
                continue
            country_count[country] = country_count.get(country, 0) + 1
    return country_count


def plot_umpire_countries(country_count):
    """Plot a bar chart of number of foreign umpires by country."""
    if not country_count:
        print("No foreign umpire data available to plot.")
        return

    countries = list(country_count.keys())
    counts = [country_count[c] for c in countries]

    plt.figure(figsize=(8, 5))
    plt.bar(countries, counts, color="skyblue", edgecolor="black")
    plt.title("Non-Indian Umpires in IPL (Count by Country)")
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("../plotting-images/umpire-country-count.png")
    plt.show()


def execute():
    """Execute the data reading, calculation, and plotting pipeline."""
    mapping_csv = "../data/umpire_countries.csv"
    country_counts = read_umpire_countries(mapping_csv)
    print(f"\nFound {len(country_counts)} foreign countries:")
    for c, n in country_counts.items():
        print(f"  {c}: {n}")
    plot_umpire_countries(country_counts)


if __name__ == "__main__":
    execute()
