# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
def sentiment():
    text="Hello, world"
    client = language.LanguageServiceClient.from_service_account_json(r"C:\Users\zliu1\projects\pen-paper\penpaper\credentials.json")

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print(sentiment.score)
    return sentiment
    #print('Text: {}'.format(text))
    #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
sentiment()
