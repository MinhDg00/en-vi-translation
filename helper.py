import os
from bs4 import BeautifulSoup

def load_data(path):
    data = []
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            data.append(BeautifulSoup(f, 'lxml'))
    return data
            
def split_data(data):
    en = []
    vi = []
    for d in data:
        i = 0
        for text in d.find_all('s'):
            if i%2 == 0:
                d1.append(text.text)
            else:
                d2.append(text.text)
            i += 1 
    return en, vi

