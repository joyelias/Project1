import requests_oauthlib
import requests

url ="https://api.twitter.com/1.1/search/tweets.json?q=Beyonce"

oauth = requests_oauthlib.OAuth1(
    "1g57GGgJ7CBOPpGooj9MUKYFk", 
    "C9aFUfRIT1Ad0nB9DN4N0Cn0iQ114kXn2t8dM72NGk0ZH1eoiz",
    "325816963-BpjzgaU98fPHtZknAK1X9Oq3QxSmflHE44cJu6hC",
    "skAgcoC7tIh2GuLReMrCx5iO60gWz0vT4sh2fnqQs4FFr"
)

response =requests.get(url, auth=oauth)

print(response.json())



