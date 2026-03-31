from nltk.sentiment.vader import SentimentIntensityAnalyzer
#imports SentimentIntensityAnalyzer from the VADER module of Natural Language Toolkit
def analyse(statement):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(statement)
    #creates a scores dictionary containing the neutralily, negativity, positivity, and overall compound score of the passed statement
    compound = scores['compound']
    #assigns the score to a variable 'compound'
    if compound < -0.3 :
        sentiment = "Stressed"
    elif compound >= -0.3 and compound <= 0.3:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"
    #predefined rules associating the score to the mood
    return compound, sentiment