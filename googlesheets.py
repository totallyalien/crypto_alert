import pygsheets

client = pygsheets.authorize(service_account_file="delta-essence-377715-cde6a7fc05d3.json")
spreadsht = client.open("Stockdatasheet")
worksht = spreadsht.worksheet("title", "Sheet1")



class Sheet:
    def __init__(self) -> None:
        self.dict={}
        pass

    def list_data(self):
        for content in worksht.get_all_records():
            self.dict[content["symbol"]]=[content["price_trig"],content["relation"],content["name"],content["row"]]
        return self.dict
    

    def delete_row(self,row_number):
        worksht.delete_rows(row_number)



