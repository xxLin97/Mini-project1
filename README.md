EC601 - MINI PROJECT 1: Sentiment-Analyser
This project is developed to analyse Twitter feeds and give an averall report of the sentiments/reviews of the people on a specific product or item which in turn is motivated from a User Story.

USER STORIES:
WORK DIVISION:
Samyak is working on Twitter API to extract and clean the data from twitter feeds to get useful data for analysis.
Zhinchao is working with the Google NLP ALI to analyse the data from Twitter API and give the final sentiment analysis.
SPRINTS:
SPRINT 1:
Define User Stories
Learn how to use GitHub and create a GitHub repository
Learn about Google NLP API and Twitter API and get access to authentication keys
Design a basic layout of the product based on the use stories
SPRINT 2:
Divide the work
Script for getting tweets from twitter feed
Script to analyse these tweets
SPRINT:
Combine both the scripts designed in Sprint 2 to create the final product
Update the final system architecture
PYTHON LIBRARIES USED:
To run this sentiment analysis app, the following libraries are required to be imported:

Google Cloud for Google NLP API
Tweepy for Twitter API
argparse for user-friendly interface
ARCHITECTURE:
This app is designed by incorporating the Twitter API and the Google Natural Language API. Python programming language is used here to write the code for this app. The code is divided into three different files:

main.py: This is python script which is used to run the Sentiment Analyser. It interacts with the files twitter.py and google_nlp.py.
twitter.py: This python script is used to extract twitter feeds based on a search parameter(a keyword), clean them so that they can be analysed using the Google NLP API.
google_nlp.py: This python script uses the Google NLP API to work on the extracted and cleaned data using the Twitter API and analyses it for sentiments to give an emotional review towards the product.
