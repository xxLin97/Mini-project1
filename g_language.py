from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Make a function called get_sentiment_score which takes tweet as the parameter, and returns the sentiment score.

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