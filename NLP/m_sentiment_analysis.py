from nltk.sentiment.vader import SentimentIntensityAnalyzer
from array import array

def analysis(message_text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(message_text)
    i=0
    x=[]
    for key in sorted(score):
        x.append(score[key])
        i=i+1
    return x