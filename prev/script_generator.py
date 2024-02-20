from newsapi import NewsApiClient
from datetime import date
from openai import OpenAI
import os


# API KEY SET UP 
newsapi = NewsApiClient(api_key='d715fab9c17e4c22a466928247e8441c')


# Get today's date a month ago. Day ? 

today = date.today()

month_ago = date(today.year, today.month - 1, today.day) if today.month != 1 else date(today.year - 1, 12, today.day)

terms = ['skincare trend', 'top beauty hacks', 'beauty trend', 'top beauty', 'top beauty trend', 'popular beauty']
# ONE WAY TO DO IT 
news_results = []
for term in terms:
    news = newsapi.get_everything(qintitle=term, 
                            from_param=month_ago, 
                            to=today,
                            language='en',
                            sort_by='popularity')
    
    for i in range(1, int(news['totalResults']/100) + 2):
        news_results += newsapi.get_everything(qintitle=term, 
                            from_param=month_ago, 
                            to=today,
                            language='en',
                            page = i,
                            sort_by='popularity')['articles']





# [removed] clauses !!
titles = [d['title'] for d in news_results]
for t in titles:
    print(f"{t}\n")
article_info = [(d['title'], d['description']) for d in news_results]


# ANOTHER WAY TO DO IT 
# Retrieve a full article talking about top beauty trends
# Things to take into account:
# 1. Paid memberships - vogue etc. 
# - These show limited content of the articles 


# GPT-3 

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You work in the digital marketing department of a beauty tech company"},
              {"role": "user", "content": f"You need to produce a three minute long video on top beauty and skincare trends. Write a video script for the voiceover of the video taking into account the latest news presented in double hashes (##): ## {article_info} ## \
               . The video script is going to be read by only one person and only include the explicit text someone is going to read. Do not include any transition information or text that should not be read. The video script should have the following structure: \
               1. Introduction: talk about how the beauty industry has changed the world. \
               2. Development: Make a top 5 list from the latest news. Identify the trends and explain each one closely \
               3. Conclusion: make an overview. "}
  ]
)

print(completion.choices[0].message)
