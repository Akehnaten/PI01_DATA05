# Librerias que voy a usar

import pandas as pd

amazon_prime = pd.read_csv('Datasets/amazon_prime_titles.csv', delimiter=',', encoding="UTF-8")
amazon_prime = amazon_prime.drop_duplicates()

disney_plus = pd.read_csv('Datasets/disney_plus_titles.csv', delimiter=',', encoding="UTF-8")
disney_plus = disney_plus.drop_duplicates()

hulu= pd.read_csv('Datasets/hulu_titles.csv', delimiter=',', encoding="UTF-8")
hulu = hulu.drop_duplicates()

netflix = pd.read_json('Datasets/netflix_titles.json', orient='columns', encoding="UTF-8")
netflix = netflix.drop_duplicates()

# Limpio los dataframes
amazon_prime['show_id'] = amazon_prime['show_id'] .replace({'[a-zA-Z ]':''}, regex=True)
amazon_prime['duration'] = amazon_prime['duration'] .replace({'[a-zA-Z ]':''}, regex=True)
amazon_prime['duration'] = amazon_prime['duration'] .fillna(0)
amazon_prime['duration'] = amazon_prime['duration'].astype('int64')
amazon_prime['show_id'] = amazon_prime['show_id'].astype('int64')
amazon_prime = amazon_prime.set_index('show_id')

disney_plus['show_id'] = disney_plus['show_id'] .replace({'[a-zA-Z ]':''}, regex=True)
disney_plus['duration'] = disney_plus['duration'] .replace({'[a-zA-Z ]':''}, regex=True)
disney_plus['duration'] = disney_plus['duration'] .fillna(0)
disney_plus['duration'] = disney_plus['duration'].astype('int64')
disney_plus['show_id'] = disney_plus['show_id'].astype('int64')
disney_plus = disney_plus.set_index('show_id')

hulu['show_id'] = hulu['show_id'] .replace({'s':''}, regex=True)
hulu['duration'] = hulu['duration'] .replace({'[a-zA-Z ]':''}, regex=True)
hulu['duration'] = hulu['duration'] .fillna(0)
hulu['duration'] = hulu['duration'].astype('int64')
hulu['show_id'] = hulu['show_id'].astype('int64')
hulu = hulu.set_index('show_id')

netflix['show_id'] = netflix['show_id'] .replace({'s':''}, regex=True)
netflix['duration'] = netflix['duration'] .replace({'[a-zA-Z ]':''}, regex=True)
netflix['duration'] = netflix['duration'] .fillna(0)
netflix['show_id'] = netflix['show_id'].astype('int64')
netflix['duration'] = netflix['duration'].astype('int64')
netflix = netflix.set_index('show_id')

# Lleno los vacios
amazon_prime = amazon_prime.fillna('Sin datos')
disney_plus = disney_plus.fillna('Sin datos')
hulu = hulu.fillna('Sin datos')
netflix = netflix.fillna('Sin datos')