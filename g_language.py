
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END language_sentiment_tutorial_imports]



def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient.from_service_account_json("/media/sf_shared_folder/creds.json")

    with open(movie_review_filename, 'r') analyze_sentiment review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)




if __name__ == '__main__':
    
    #analyze(args.movie_review_filename)
    analyze("/media/sf_shared_folder/reviews/bladerunner-mixed.txt")
