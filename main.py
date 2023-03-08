# stock_alert
import requests
import time
import os
import datetime as dt
from stock_list import StockList
from stock_price import StockPrice
from mail_alert import MailAlert
from news import News
from call_sms import Call_Sms
from googlesheets import Sheet
from api_keys import MAIL_ID,MAIL_PASS,TO_NUMBER,TO_MAIL


#returns symbol dic
while True:

    now = dt.datetime.now()
    current_hour =now.hour

    
    raw_data = Sheet()
    stock_dic=raw_data.list_data()
    print(stock_dic)
    price_list = StockPrice() 
    price_data = price_list.price(stock_dic) 
    mail = MailAlert(MAIL_ID,TO_MAIL,MAIL_PASS) #init mail login
    
    for i in price_data:
        if (stock_dic[i][1])==">":
            if float(price_data[i][0])>float(stock_dic[i][0]):
                    twil = Call_Sms(TO_NUMBER)                      
                    if 22 < current_hour < 8:
                         twil.Call_alert(f"{i} : {price_data[i][0]}")

                    else:
                        twil.Sms_alert(f"{i} : {price_data[i][0]}")
                        print(price_data[i])
                        
                    news=News(stock_dic[i][2])
                    news_raw=news.news_list()
                    if len(news_raw)==1:
                        news_list1=[news_raw[0]["url"],news_raw[0]["title"],news_raw[0]["urlToImage"]]
                        mail.html_update(i,price_data[i][0],news_list1)
                        mail.send_mail()
                    elif len(news_raw)>1:
                        news_list1=[news_raw[0]["url"],news_raw[0]["title"],news_raw[0]["urlToImage"]]
                        news_list2=[news_raw[1]["url"],news_raw[1]["title"],news_raw[1]["urlToImage"]]
                        mail.html_update(i,price_data[i][0],news_list1,news_list2)
                        mail.send_mail()
                    else:
                        print("empty")
                        mail.price_mail_alert(i,price_data[i][0]) 

                    raw_data.delete_row(int(stock_dic[i][3]))


        elif (stock_dic[i][1])=="<":
            if float(price_data[i][0])<float(stock_dic[i][0]):
                    twil = Call_Sms(TO_NUMBER)                      
                    if 22 < current_hour < 8:
                         twil.Call_alert(f"{i} : {price_data[i][0]}")

                    else:
                        twil.Sms_alert(f"{i} : {price_data[i][0]}")
                        print(price_data[i])
                        
                    news=News(stock_dic[i][2])
                    news_raw=news.news_list()
                    print(len(news_raw))
                    if len(news_raw)==1:
                        news_list1=[news_raw[0]["url"],news_raw[0]["title"],news_raw[0]["urlToImage"]]
                        mail.html_update(i,price_data[i][0],news_list1)
                        mail.send_mail()
                        print("n1")
                    elif len(news_raw)>1:
                        news_list1=[news_raw[0]["url"],news_raw[0]["title"],news_raw[0]["urlToImage"]]
                        news_list2=[news_raw[1]["url"],news_raw[1]["title"],news_raw[1]["urlToImage"]]
                        mail.html_update(i,price_data[i][0],news_list1,news_list2)
                        mail.send_mail()
                        print("n2")
                    else:
                        print("empty")
                        mail.price_mail_alert(i,price_data[i][0])   

                    raw_data.delete_row(int(stock_dic[i][3]))   

    
    time.sleep(20)
                     



        







