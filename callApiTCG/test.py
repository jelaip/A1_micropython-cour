api_key = "4455b71fd4f76a3327dcf08d93c4c457909f866e54660ff6699307f044bc8331"


import requests

url = "https://apitcg.com/api/one-piece/cards?name=luffy"

r = requests.get(url, headers={"x-api-key": api_key})
print(r.json())

