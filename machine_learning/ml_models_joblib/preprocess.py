# Text Preprocessing
import re

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from bs4 import BeautifulSoup



print(__name__)

class Preprocess():
    
    def __init__(self):
        self.eng_stopword_list = set(stopwords.words("english"))
        # 'no' and 'not' may be useful in sentiment analysis
        self.eng_stopword_list.remove('no')
        self.eng_stopword_list.remove('not')
    
    
    def word_tokenize(self, text):
        self.tokenized_text = word_tokenize(text)
    
        return self.tokenized_text
    
    
    def make_lowercase(self, text):
        self.lowercase_text = text.lower()
        
        return self.lowercase_text
    
    
    def remove_stopwords(self, tokenized_text):
        self.stopwords_removed = [element for element in tokenized_text if element.lower() not in self.eng_stopword_list]
        self.stopwords_removed = " ".join(self.stopwords_removed)
        
        return self.stopwords_removed
    
    
    def remove_numbers(self, text):
        regex = RegexpTokenizer('[^\d\s\n]+')
        self.numbers_removed = regex.tokenize(text)
        self.numbers_removed = " ".join(self.numbers_removed)
        
        return self.numbers_removed
        
        
    def remove_special_characters(self, text):
        regex = RegexpTokenizer('[a-zA-Z0-9]+')
        self.special_characters_removed = regex.tokenize(text)
        self.special_characters_removed = " ".join(self.special_characters_removed)
        
        return self.special_characters_removed
    
    
    def remove_html_tags(self, text):
        html = BeautifulSoup(text, "html.parser")
        self.html_tags_removed = html.get_text()
#         self.html_tags_removed = processor.remove_special_characters(self.html_tags_removed)
        
        return self.html_tags_removed 
    
    
    def remove_url(self, text):
        url_pattern = r"((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+)"
        self.url_removed = re.sub(url_pattern, "", text)
#         self.url_removed = processor.remove_special_characters(self.url_removed)
        
        return self.url_removed

    
def select_parameters(text, make_lowercase=False, remove_stopwords=False, remove_numbers=False, 
                      remove_html_tags=False, remove_special_characters=False, remove_url=False):
    
    processor = Preprocess()
    
    if text == ">":
        return "***** SAZAN.AVI ***** HA BU YEM DUR ***** \n Ne meraklı milletiz ya"
    
    
    if remove_url:
        text = processor.remove_url(text)
    
    if remove_html_tags:
        text = processor.remove_html_tags(text)
        
    if remove_special_characters:
        text = processor.remove_special_characters(text)
    
    if remove_numbers:
        text = processor.remove_numbers(text)
    
    if make_lowercase:
        text = processor.make_lowercase(text)
    
    if remove_stopwords:
        tokenized_text = processor.word_tokenize(text)
        text = processor.remove_stopwords(tokenized_text)
        
    return text
    

if __name__ == "__main__":    
    processor = Preprocess()
