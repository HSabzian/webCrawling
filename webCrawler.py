
## A webcraeler for Finding the number of a target word in a web page
import requests
from bs4 import BeautifulSoup

def count_word_occurrences(url, word):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    text = soup.get_text().lower()
    word_count = text.count(word.lower())
    return word_count

url = 'https://en.wikipedia.org/wiki/John_von_Neumann'  ## selected web page
word = 'math'  ## target word
word_count = count_word_occurrences(url, word)
print(f'The word "{word}" occurs {word_count} times on the page.')
