import os
import urllib.request as ulib
import requests
from bs4 import BeautifulSoup
import getpass
all_link = []


def download_google(word):
    url = 'https://www.google.com/search?tbm=isch&q=' + word
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    for raw_img in soup.find_all('img')[:11]:
        link = raw_img.get('src')
        all_link.append(link)
    return all_link


def save_img(url, directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
    for i, link in enumerate(url):
        path = os.path.join(directory, "{:02}.jpg".format(i))
        try:
            ulib.urlretrieve(link, path)
        except:
            print("Failed..")


if __name__ == '__main__':
    word = input("Input key word: ")
    link = download_google(word)
    save_img(link, "/home/"+getpass.getuser()+"/Downloads/")
