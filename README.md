± IPL Data Analytic Projects

± Project Overview

This repository contains Python scripts for analyzing and visualizing IPL data.

Key insights generated include:

Umpire distributions (foreign vs Indian)

Team runs and scoring trends

Match outcomes

Other IPL statistics

The scripts do not use heavy libraries like pandas or NumPy. Only Python’s built-in modules (csv) and matplotlib for visualization.

All code is organized under plotting-logic-code/, raw data is in data/, and generated plots are saved in plotting-images/.


± Installation & Requirements

Install Python 3.10+

Install dependencies:

pip install -r requirements.txt


± Project Structure

Folder / File	         Description
data/	Raw CSV/XLSX      data files
plotting-logic-code/	  Python scripts for analysis
plotting-images/	      Generated plot images (ignored by Git)
requirements.txt	      Lists required Python libraries
.gitignore	              Ignores data files, plots, venv, IDE files
README.md	              Project documentation


▶ How to Run

Run any script from the project root:

# Example: run umpire country plot script
python plotting-logic-code/umpire_country_plot.py


Replace umpire_country_plot.py with any other script in plotting-logic-code/.

± Scripts Overview

Script Name	                    Description
umpire_country_plot.py	         Reads data/umpire_countries.csv and plots number of foreign umpires
team_run_plot.py	             Plots total runs per team
matches_won_byteam_plot.py	     Visualizes number of matches won by each team
stacked_bar_chart_plot.py	     Creates stacked bar charts for different match statistics
total_matches_year_plot.py	     Plots total matches per year
top_10_rcb_batsman_plot.py	     Visualizes top 10 RCB batsmen stats
most_economical_bowler_plot.py	 Plots top economical bowlers

All scripts follow the same pattern:

calculate() – read & compute data

plot() – generate visualization

execute() – orchestrates calculate + plot

Uses csv.DictReader for clean data handling

Descriptive variable names (no single-character names)

Minimal memory usage by performing computations directly in the CSV reading loop

Compatible with linters (flake8, pylint)


± Notes & Best Practices


.gitignore prevents tracking of large CSVs, generated plots, virtual environments, and IDE files

requirements.txt contains only the library actually used (matplotlib)

Code is ready for linting and follows best practices for readability and maintainability