import pandas as pd
class StockList:

    def __init__(self,filename) -> None:
        self.filename=filename
        self.dic={}

    def csv_to_list(self):
        self.data = pd.read_csv(self.filename)
        for (i,j) in self.data.iterrows():
            self.dic[j.symbol]=j.price_trig
        return self.dic
        