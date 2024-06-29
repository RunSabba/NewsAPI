import requests

#using the requests.get to pull the data from the site. i can adjust the date,language, and enter the API key at the end of the string. Issues pulling info from too far back in time.
r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-6-25&to=2024-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")

#using the content variable to have our variable "r" convert the contents of the api data into JSON Format.
content = r.json()

#using this to print what data type we're printing. "Its a dictionary, that also has lists with nested dictionaries"
#print (type(content))

#here we're printing the contents, but we're going into the articles list first, then the 8th article, and then the description of the article.
print (content["articles"][7]["description"])

#articles arent printing in the correct order. will work on imporving the code to do so tomorrow.