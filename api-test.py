import requests

url ="https://api.spoonacular.com/recipes/search?diet=gluten%20free&apiKey=4cc34612813a4bafa176a17b31e1c6e1"

response = requests.get(url)
print(response.text)

