import requests

#using the requests.get to pull the data from the site. i can adjust the date,language, and enter the API key at the end of the string. Issues pulling info from too far back in time.
""""r = requests.get("https://newsapi.org/v2/everything?qInTitle=sports&from=2024-6-26&to=2024-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")

#using the content variable to have our variable "r" convert the contents of the api data into JSON Format.
content = r.json()

#using this to print what data type we're printing. "Its a dictionary, that also has lists with nested dictionaries"
#print (type(content))

#placing the articles within my content variable in a new variable named "articles"
articles = content["articles"]
print(type(articles))

#using a for loop to iterate thru my articles variable and only print the Titles and articles. 
for article in articles:
  print("*TTILE\n", article["title"], "\n*DESCRIPTION\n", article["description"])
"""

""""def get_news(topic, from_date , to_date, language="en",api_key="890603a55bfa47048e4490069ebee18c"):
  url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE: '{article['title']}'\nDESCRIPTION: '{article['description']}'\n")
  return results

print (get_news(topic='space',from_date='2024-5-26',to_date='2024-6-25'))
"""

