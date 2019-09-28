def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
               .Document(content=tweet,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score

def analyze_tweets(keyword, total_tweets):
    score = 0
    tweets = search_tweets(keyword,total_tweets)
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        print('Tweet: {}'.format(cleaned_tweet))
        print('Score: {}\n'.format(sentiment_score))
    final_score = round((score / float(total_tweets)),2)
    return final_score

def send_score(final_score):
  if final_score <= -0.25:
    status = 'NEGATIVE'
  elif final_score <= 0.25:
    status = 'NEUTRAL'
  else:
    status = 'POSITIVE'
  print("The atitude of"+str(keyword)+"is"+status)


def main():
  keyword=input("keyword that you want to search")
  get_sentiment_score(result)
  analyze_tweets(keyword,50)
  send_score(final_score)
    
if __name__ == '__main__':
    main()    
