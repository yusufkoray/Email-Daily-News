import requests
from send_email import  send_email

topic="tesla"
api_key="4208cc1a4344490abf32a0d973ba1d3e"
url="https://newsapi.org/v2/everything?" \
    f"q={topic}&from=2025-01-02&" \
    "sortBy=publishedAt" \
    "&apiKey=4208cc1a4344490abf32a0d973ba1d3e&"\
    "language=tr"
# we should add '&'.

request=requests.get(url)
#content=request.text #string
content=request.json() #dictionary

print(content)
#print(content["articles"])

#task
#title ve description'ı kendi email'ine gonder

body=""

for article in content["articles"][:20]:
    if article["description"] is None:
        article["description"]=str(article["description"])
        article["description"]=""
    body+="Subject: Today's news:"\
            +str(article["title"])+"\n" + str(article["description"])+article["url"]+"\n"+2*"\n"
body=body.encode("utf-8")
send_email(body)

