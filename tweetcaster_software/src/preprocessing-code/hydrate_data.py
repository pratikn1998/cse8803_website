import json
import tweepy
import math
import pandas as pd

def hydrate_full_dataset():
    chunksize = 10 ** 6
    df_iterator = pd.read_csv(
        '../data/2021_cleaned_dataset_geo.tsv',
        delimiter='\t',
        chunksize=chunksize
    )

    batch_size = 100
    df_hydrated = pd.DataFrame()

    counter = 1
    for chunk in df_iterator:
        chunk['text'] = ''
        N = len(chunk)
        print('Current chunk has {} entries.'.format(N))
        batches = int(math.ceil(N / batch_size))
        valid_ids = []
        valid_contents = []
        print('Hydrating chunk #{}'.format(counter))

        for i in range(batches):
            if (i + 1) * batch_size <= N:
                tweet_ids = chunk['tweet_id'].values[i * batch_size: (i + 1) * batch_size]
            else:
                tweet_ids = chunk['tweet_id'].values[i * batch_size:]
            query = ''
            for id in tweet_ids:
                query += str(id)
                query += ','
            query = query[0: -1]
            tweets = client.get_tweets(query).data
            for tweet in tweets:
                if tweet is not None:
                    valid_ids.append(tweet.id)
                    valid_contents.append(tweet.text.replace('\n', '\\n'))
            print('Progress in chunk #{}: {:.4%}'.format(counter, (i + 1) / batches))
        hydrated_chunk = chunk[chunk['tweet_id'].isin(valid_ids)]
        hydrated_chunk.loc[:, 'text'] = valid_contents
        nan_value = float('NaN')
        hydrated_chunk.replace('', nan_value, inplace=True)
        hydrated_chunk = hydrated_chunk.dropna(subset=['text'])
        print('Finished hydrating chunk #{}'.format(counter))
        counter += 1
        df_hydrated = df_hydrated.append(hydrated_chunk)

    df_hydrated.to_csv(
        '../data/2021_hydrated_dataset.tsv',
        sep='\t',
        index=False
    )

def hydrate_dataset_part(part_num):
    usa_df = pd.read_csv(
        '../data/part{}.tsv'.format(part_num),
        delimiter='\t'
    )
    usa_df['text'] = ''
    N = len(usa_df)
    print('Current data has {} entries.'.format(N))

    batch_size = 100
    batches = int(math.ceil(N / batch_size))

    valid_ids = []
    valid_contents = []

    print('Hydrating...')
    for i in range(batches):
        if (i + 1) * batch_size <= N:
            tweet_ids = usa_df['tweet_id'].values[i * batch_size: (i + 1) * batch_size]
        else:
            tweet_ids = usa_df['tweet_id'].values[i * batch_size:]

        query = ''
        for id in tweet_ids:
            query += str(id)
            query += ','
        query = query[0: -1]

        tweets = client.get_tweets(query).data

        for tweet in tweets:
            if tweet is not None:
                valid_ids.append(tweet.id)
                valid_contents.append(tweet.text.replace('\n', '\\n'))
        print('Progress: {:.4%}'.format((i + 1) / (batches)))

    hydrated_df = usa_df[usa_df['tweet_id'].isin(valid_ids)]
    hydrated_df.loc[:, 'text'] = valid_contents
    nan_value = float('NaN')
    hydrated_df.replace('', nan_value, inplace=True)
    hydrated_df = hydrated_df.dropna(subset=['text'])
    hydrated_df.to_csv(
        '../data/part{}_hydrated.tsv'.format(part_num),
        index=False,sep='\t'
    )
    print('Finished hydrating')


if __name__ == '__main__':
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    BEARER_TOKEN = ''
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''

    with open('api_keys.json', 'r') as f:
        data = json.load(f)
        CONSUMER_KEY = data['consumer_key']
        CONSUMER_SECRET = data['consumer_secret']
        BEARER_TOKEN = data['bearer_token']
        ACCESS_TOKEN = data['access_token']
        ACCESS_SECRET = data['access_secret']

    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET,
        wait_on_rate_limit=True
    )

    part = 5
    hydrate_dataset_part(part)

