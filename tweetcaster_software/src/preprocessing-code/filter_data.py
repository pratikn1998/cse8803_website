import pandas as pd

if __name__ == '__main__':
    df_2021_geo = pd.read_csv(
        '../data/2021_cleaned_dataset_geo.tsv',
        delimiter='\t'
    )
    df_usa = df_2021_geo[df_2021_geo['country_place'] == 'US']
    df_usa.to_csv('../data/2021_usa_dataset.tsv', sep='\t', index=False)