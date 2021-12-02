# Welcome to the Demo!

Hello there! Welcome to the demo of TweetCaster! This section will guide you on how to use our project and see it in action on a small dataset (don't worry, we have done most of the dataset heavylifting for you). But before we move forward with that, we would highly recommend you to open this notebook in Google Colab. There are certain features (like downloading datasets) that might work only on that platform. Having said this, let's begin!

## Step 0: Open the Notebook
Naviagate to .tweetcaster_software/src/TweetCaster.ipynb and open the notebook in Google Colab. 

## Step 1: Download the dependencies
There are a set of libraries that might need to be downloaded and installed and a bunch of other libraries that you might just need to import. To do this, just run the two cells we have provided in the Project Setup section. They will automatically install everything for you while you just sit back enjoy the satisfying scene of a moving progress bar. :)

## Step 2: Pre-process the dataset
The dataset will need to be pre-processed before we can show you the magic of TweetCaster. This will hydrate the dataset and also get rid of any not-so-useful hashtags or retweet tags that Twitter occassionally adds in the tweet body. Just run the cells in dataset preparation starting from top going to the bottom one by one and you should be on your way to trying out our very first experiment. This section also has a helper that we use to show you pretty charts in our notebook.

## Step 3: Tweet Sentiment Analysis
You would need to run sentiment analysis on the tweets loaded in the dataset. This is a crucial datapoint for our project and MUST NOT be skipped for error-free run. Execute all cells in Tweet Sentiment Analysis section starting from top going all the way to the bottom one by one. Getting the subjectivity and polarity, in our experience, takes about 2 - 3 minutes. Please be patient while it runs - coffee break! Once everything is done executing, you might see a couple of graphs pop up. One of them tells you the sentiment distribution in our dataset and the other one will show you the prominent words through a word cloud.

## Step 4: Adding Step 3 Results to Dataset
Alright, this is the last boring section, I promise! All you need to do is execute the cells in the given order in the Dataset Pre-processing after Sentiment Analysis section.

## Step 5: Experimentation, Evaluation, and a Cup of Tea (OPTIONAL)
This section just shows all the approaches we tried and displays the RMSE returned by each. This step is completely optional and MAY BE SKIPPED if you would like to go directly to our main approach.

### Step 5a: Regression using Sentiment Analysis (OPTIONAL)
We have set up this section to run linear regression on the input and display the graph of predictions and true case numbers. At the end of the section, the root mean squared error (RMSE) value is also printed. Be sure to execute all cells in this section in the given order to see the expected results.

### Step 5b: Time Series Models (OPTIONAL)
We implemented some time series models for you to check out. As of now, we have ARIMA, OLS, an ensemble of the two methods and an ensemble of the two with the linear regression model from Step 5a loaded in. You may start from the top and work your way to the bottom. Each subsection will display the prediction and true values graph and print out the RMSE value.

### Step 5c: Neural Network with Tweet Metadata and Sentiment Analysis (OPTIONAL)
We implemented the neural network we suggest in our report with just the tweet metadata and sentiment analysis data. We have already pre-loaded all the hyper-parameters for you so that you can just hit the execute button on all the cells in this section and watch everything run.

## Step 6: Tweet Vectorization (REQUIRED)
The next section involves tweet vectorization. Simply run all the cells in Tweet Vectorization section and you should be good to go.
<b>Important:</b> If you would like to use the TF-IDF embeddings, be sure to set the TF-IDF `MAX_FEATURES` variable to the maximum number of features you would like to see. We have tested it with 200 and 500 features.

### Step 5d: Neural Netowrk with Tweet Encoding Only (OPTIONAL)
While playing around with the data, we implemented the neural network on the tweet encoding data as well. This section does not assume access to the tweet metadata or its sentiment value. Feel free to run this section entirely if you would like to see how well does the model perform without rest of the data we have gathered so far. Apart from the usual data, you may also see a smoothed graph. This graph is just a 5-days moving average of the graph you were seeing earlier.

## Step 7: TweetCaster - Neural Network with Tweet Encoding, Metadata and Sentiment Values (MAIN APPROACH)
This is the main approach of our work. You may play around with the embedding we use for this part. Please read the note in the section to see exactly how to change between embedding. As of now, we have it set to execute everything using BERTweet embedding. We currently have it set to also train four models (with different sizes of the rolling window), but the code block with show just one set of graphs (for the rolling window of 7 days, since it performs the best). Change the `qualifying_entry` to (`rolling_window_length`, 7) where `rolling_window_length` can take values of 7, 14, 21 and 28 will let you see the other graphs as well. Be sure to execute all the code blocks in this section in the given order to avoid any errors.

## Thank You for Checking Out TweetCaster!
Alright, that was all! Thanks for reading the demo, and I hope that you enjoyed checking out our project. 