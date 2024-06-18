import snscrape.modules.twitter as sntwitter
import pandas as pd


#query to script the tweets
twit_query = "RejectFinanceBill2024"

#query to script the tweets
max_tweets = 10

#list to store scrapped tweets
tweets= []


# # Using TwitterSearchScraper to scrape data and append tweets to list
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper(twit_query).get_items()):
#     print(tweet)
#     break
#     if i >= max_tweets:
#         break
#     tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount])
    
# twt_df = pd.DataFrame(tweets, columns = ['Date', 'Twitter ID', 'Content','Username','Likes', 'Retweet'])    


def scrape_tweets(query, max_tweets):
    tweets= []
    try:
        # for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{twit_query}').get_items()):
        print(f'Scarpping for : {twit_query} has began')
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(twit_query).get_items()):
            if i>= max_tweets:
                break
            tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount])
    except Exception as e:
        print(f'An error occured : {e}')
    return tweets

y = scrape_tweets(twit_query, max_tweets)




   


   