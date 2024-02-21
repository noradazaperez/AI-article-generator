# Publishing to Medium using the latest news. 

In this project, we have developed a Python script that retrieves the news articles about the latest skincare trends and 
generates an article, using OpenAI's ChatGPT AI model. The program will also post said article to a given Medium profile as a 
draft. 

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Google News API](https://www.news.google.com): set up a Google News API and generate an API token.
- [OpenAI API](https://www.openai.com): set up an OpenAI Plus account. 
- [Medium API](https://www.medium.com): sign up and create an account in the Medium website. 

### Installing

A step by step series of examples that tell you how to get a development
environment running

Install the Google News library

    pip install newsapi-python

Install the OpenAI library

    pip install openai

Install the https request library

    pip install requests

* Set up api keys in Ubuntu/MacOS:

1. **Google News API:**
```
export NEWS_API={key_value}
```

2. **OpenAI API:**
```
export OPENAI_API_KEY={key_value}
```

3. **Medium API:**
```
export MEDIUM_API={key_value}
```

## Running the tests

By running the following command:

    python3 script_generator.py



An article will be generated and posted to the given Medium account. 
The script gives a link to the generated image as an output, as well as an 
error code for uploading the article. 

## Authors

  - **Nora Daza Pérez** - *developed and designed the code.*




