from bs4 import BeautifulSoup
import requests
import pandas as pd

# Make request object for beautiful soup
url = "https://www.vocabulary.com/lists/194479"
page = requests.get(url)

# Create the soup
soup = BeautifulSoup(page.content, 'lxml')

# Locate relevant nodes and make list
words = soup.find_all('a', class_='word dynamictext')
definitions = soup.find_all('div', class_='definition')

# Loop over list to extract text
word_list = []
def_list = []
for word in words:
    word_list.append(word.text)

for def_ in definitions:
    def_list.append(def_.text)

# Chuck everything into a final table
table = pd.DataFrame()
table['word'] = word_list
table['definition'] = def_list

#Save as csv file
table.to_csv(r'C:\Users\Anas Khan\OneDrive - The University of Melbourne\Desktop\Preparation\Gre\gre_high_frequency_words.csv')
