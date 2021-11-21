# Importing the packages required
from bs4 import BeautifulSoup
import requests

# create a function to extract only text from <p> tags

def get_only_text(url):
    ''' return the title and text from the headline of 
    the spesfied url'''

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text , soup.find_all('p')))
    title = ' '.join(soup.title.stripped_strings)
    return title, text

# calling the function with spesfied url

text = get_only_text('https://www.voxmedia.com/2021/11/19/22791332/the-second-season-of-vox-and-vox-media-studios-the-mind-explained-premieres-today-on-netflix')

print(text) # verifying the results

print(len(str.split(text[1]))) # getting the number of words in the text extracted

print(text[0])



