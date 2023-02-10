import requests

class StockPrice:
    def __init__(self) -> None:
        self.price_dic={}

    def price(self,dic):
        for i in dic:
            self.response=requests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={i}")
            self.price_dic[self.response.json()['symbol']]=[self.response.json()['price']]
        return self.price_dic
    

