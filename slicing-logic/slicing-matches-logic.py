import pandas as pd
file = pd.read_csv('data/deliveries.csv')
for i in range(1,637):
    match_i=file[file['match_id'] == i]
    match_i.to_csv(f'sliced_deliveries/match{i}.csv', index = False)