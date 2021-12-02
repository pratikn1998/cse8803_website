import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('../data/2021_cleaned_dataset_geo.tsv', delimiter='\t')
    df = df.loc[df['country_place'] == 'US']

    df_part_1 = df.iloc[0:80000]
    df_part_2 = df.iloc[80000:160000]
    df_part_3 = df.iloc[160000:240000]
    df_part_4 = df.iloc[240000:320000]
    df_part_5 = df.iloc[320000:400000]

    df_part_1.to_csv('../data/part1.tsv', sep='\t', index=False)
    df_part_2.to_csv('../data/part2.tsv', sep='\t', index=False)
    df_part_3.to_csv('../data/part3.tsv', sep='\t', index=False)
    df_part_4.to_csv('../data/part4.tsv', sep='\t', index=False)
    df_part_5.to_csv('../data/part5.tsv', sep='\t', index=False)
