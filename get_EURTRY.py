from bs4 import BeautifulSoup as soup
import requests
import numpy as np
import re
import pandas as pd
from requests.api import head


def get_EURTRY():
    """
    This funtion fetches Euro/TRY ratio from https://www.bloomberght.com.
    """
    # Requesting the page

    headers = {"user-agent":"Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18"}
    url = "https://www.bloomberght.com/doviz/euro"
    respond = requests.get(url,headers=headers)
    
    # Scraping the content

    bsobj = soup(respond.content,'lxml')
    ratio = bsobj.find_all('small',{'data-secid':'EURTRY Curncy',"data-type":"son_fiyat"})[0].string

    return float(ratio.replace(',','.'))