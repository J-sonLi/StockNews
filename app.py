from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from config import useragent


url = 'https://finviz.com/quote.ashx?t='

#insert ticker symbol 
ticker = ''

agent = {'User-Agent':useragent}

source = requests.get(url+ticker, headers=agent)

soup = BeautifulSoup(source.content, 'lxml')

table = soup.find_all(class_='news-link-left')

analyzer = SentimentIntensityAnalyzer()

newstitles=[]

#add title to list
for titles in table:
    #print(titles.get_text())
    newstitles.append(titles.get_text())

#prints sentiment of news title (neg,neu,pos)
for sentence in newstitles:
    score=analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(score)))
