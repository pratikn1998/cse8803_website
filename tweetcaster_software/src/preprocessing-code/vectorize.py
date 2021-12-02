import pandas as pd
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectorization(df, max_features):
    vector = TfidfVectorizer(
        sublinear_tf=True,
        max_features=max_features,
        token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b'
    )
    X = vector.fit_transform(df['text'].values)
    X_col = vector.get_feature_names()
    feature_df = pd.DataFrame.sparse.from_spmatrix(X, columns=X_col)
    feature_df['tweet_id'] = df['tweet_id']
    feature_df.to_csv(
        '../data/2021_usa_dataset_{}_tfidf.csv'.format(max_features),
        index=False
    )

def tfidf_vectorization_tweet_tokenizer(df, max_features):
    tt = TweetTokenizer(preserve_case=False)
    vector = TfidfVectorizer(
        sublinear_tf=True,
        max_features=max_features,
        token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b',
        tokenizer=tt.tokenize
    )
    X = vector.fit_transform(df['text'].values)
    X_col = vector.get_feature_names()
    feature_df = pd.DataFrame.sparse.from_spmatrix(X, columns=X_col)
    feature_df['tweet_id'] = df['tweet_id']
    feature_df.to_csv(
        '../data/2021_usa_dataset_{}_tfidf_tweet_tokenizer.csv'.format(max_features),
        index=False
    )

if __name__ == '__main__':
    df = pd.read_csv(
        '../data/2021_usa_dataset_hydrated.tsv',
        delimiter='\t',
        lineterminator='\n'
    )

    max_features = 500

    tfidf_vectorization_tweet_tokenizer(df, max_features)


