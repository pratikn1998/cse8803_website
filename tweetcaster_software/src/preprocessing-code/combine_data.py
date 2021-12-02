from os import sep
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame()

    df1 = pd.read_csv(
        '../data/part1_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n')
    df2 = pd.read_csv(
        '../data/part2_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n')
    df3 = pd.read_csv(
        '../data/part3_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n')
    df4 = pd.read_csv(
        '../data/part4_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n')
    df5 = pd.read_csv(
        '../data/part5_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n')

    df = df.append(df1)
    df = df.append(df2)
    df = df.append(df3)
    df = df.append(df4)
    df = df.append(df5)

    print(df.shape)
    df.to_csv('../data/2021_usa_dataset_hydrated.tsv', sep='\t', index=False)