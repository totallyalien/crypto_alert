import requests

pram={
    "apiKey":"3f0f8dce35a647618e9d188c42dddbf0"
}

class News:
    def __init__(self,keyword) -> None:
        self.response=requests.get(url=f"https://newsapi.org//v2/top-headlines?q={keyword}",params=pram)
        self.data = self.response.json()["articles"]
        print(self.data)


a=News("eth")