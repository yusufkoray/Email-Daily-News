import requests

api_key="4208cc1a4344490abf32a0d973ba1d3e"
url="https://newsapi.org/v2/everything?" \
    "q=tesla&from=2024-12-30&sortBy=publishedAt&apiKey" \
    "=4208cc1a4344490abf32a0d973ba1d3e"

request=requests.get(url)
#content=request.text #string
content=request.json() #dictionary

#print(content["articles"])

for article in content["articles"]:
    print(article["title"])
    print(article["description"])