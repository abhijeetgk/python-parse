import urllib2
import csv
from bs4 import BeautifulSoup
class DataHandler:
    
    def __init__(self):
        self.url_pages = {
            "Home ":'https://www.moneycontrol.com/',
            "Market":'https://www.moneycontrol.com/stocksmarketsindia/',
            "Mf Home":'https://www.moneycontrol.com/mutualfundindia/'
        }
        self.url_csv = {
            "Historic BSE Infosys":"http://www.moneycontrol.com/tech_charts/bse/his/it.csv",
            "Historic NSE Infosys":"http://www.moneycontrol.com/tech_charts/nse/his/it.csv",
            "Historic Indices Sensex":"http://www.moneycontrol.com/tech_charts/bse/his/sensex.csv",
            "Historic Indices Nifty":"http://www.moneycontrol.com/tech_charts/nse/his/nifty.csv"
        }
    
    def get_last_element_timestamp(self,url):
        conn = urllib2.urlopen(url)
        html = conn.read()
        soup = BeautifulSoup(html,"lxml")
        elements = soup.find_all('div')[-1]
        return elements.text

    def historic_data(self,url):
        csv_data = urllib2.urlopen(url)
        csv_reader = list(csv.reader(csv_data, delimiter=','))
        return ([csv_reader[-1][0],csv_reader[-1][1]])

    def print_page_timestamp(self):
        data_arr=[]
        for page,url_value in self.url_pages.items():
            data_arr.append({page:self.get_last_element_timestamp(url_value)})
        
        return data_arr
    
    def print_historic_csv_data(self):
        data_arr=[]
        for page,url_value in self.url_csv.items():
            data_arr.append({page:self.historic_data(url_value)})
        return data_arr