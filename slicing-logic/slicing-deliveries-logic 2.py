import pandas as pd
file = pd.read_csv('data/deliveries.csv')
for i in range(2008,2018):
    season_i=file[file['season'] == i]
    season_i.to_csv(f'sliced_matches/match{i}.csv', index = False)