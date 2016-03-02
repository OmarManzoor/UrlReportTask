import re
import string
import sys
import urllib
from bs4 import BeautifulSoup


__author__ = 'Omar Salman'

# TODO: Can you please inherit this from "object"
class UrlReport():

    def __init__(self, url):

        self.url = url
        self.html = get_html(url)
        self.soup = ''
        self.soup_text = ''

    def is_valid(self):
        if not self.html:
            return False
        return True

    def reset_url(self,url):

        self.url = url
        self.html = get_html(url)
        self.soup = ''
        self.soup_text = ''

    def get_content_size(self):
        # TODO: You don't have to check for "self.html" in every function. because if there is no self.html
        # these functions will not be called ever. is_valid() function will quit the program already. 
        if self.html:
            if not self.soup_text:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            return len(self.soup_text)
        else:
            print 'The url given is not valid'

    def get_word_count(self):
        # TODO: Same, no need to check here
        if self.html:
            if not self.soup_text:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            return len(re.findall('\w+', self.soup_text))
        else:
            print 'The url given is not valid'

    def get_unique_word_count(self):
        # TODO: Also, we don't usually leave a white space below the function in python.
        if self.html:
            if not self.soup_text:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            return len(set(re.findall('\w+', self.soup_text.lower().encode('utf-8'))))
        else:
            print 'The url given is not valid'

    def get_alphabet_count(self):

        if self.html:
            if not self.soup_text:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            # TODO: Variable names should be more readable. "c" is not a proper name
            return len([c for c in self.soup_text if c in string.ascii_letters])
        else:
            print 'The url given is not valid'

    def meta_tag_count(self):

        if self.html:
            if not self.soup:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            return len(self.soup.find_all('meta'))
        else:
            print 'The url given is not valid'

    def get_five_most_frequent_words(self):

        if self.html:
            if not self.soup_text:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            # Nice :)
            words = re.findall('\w+', self.soup_text.lower().encode('utf-8'))
            words_dict = {}

            for each in words:
                words_dict[each] = words_dict.get(each, 0) + 1

            words = sorted(words_dict.keys(), key=words_dict.get, reverse=True)
            # Awesome..
            top_five = words[:5]
            return ', '.join(top_five)
        else:
            print 'The url given is not valid'

    def get_anchor_tag_count(self):

        if self.html:
            if not self.soup:
                self.soup, self.soup_text = initialize_beautiful_soup(self.html)
            return len(self.soup.find_all('a'))
        else:
            print 'The url given is not valid'


def get_html(url):

    try:
        html = urllib.urlopen(url).read()
        return html
    except:
        print "The url given is not valid"
        return ''

# TODO: We should move these functions in a separate class if they don't belong to above class. 
def initialize_beautiful_soup(html):

    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    all_text = soup.get_text()
    return (soup, all_text)


def format_text(text):

    text = re.sub('\s+', ' ', text).strip()
    text = "".join(c for c in text if c not in ('!','.',':',',',))
    return text


def main(url):

    report = UrlReport(url)
    # TODO: Since we are already checking and validating the "url" in this function. 
    # no need to make the html check in every other function. Below condition will prevent the other codes to run. 
    if report.is_valid():
        print "Total Content Size of page '" + url + "' is ",
        print report.get_content_size()
        print "Total Word Count on page '" + url + "' is ",
        print report.get_word_count()
        print "Total Count of Unique Words on page '" + url + "' is ",
        print report.get_unique_word_count()
        print "Total Count of Meta Tags on page '" + url + "' is ",
        print report.meta_tag_count()
        print "Top 5 Most Frequent words on page '" + url + "' are ",
        print report.get_five_most_frequent_words()
        print "Total Count of Anchor Tags on page '" + url + "' is ",
        print report.get_anchor_tag_count()
    else:
        print "Please use a url of the form http://www.------.com"


if __name__ == '__main__':

    url = sys.argv[1]
    main(url)


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## a couple of test cases for checking

#a = UrlReport('')
#a.check()
#testUrl = 'http://www.yahoo.com'
#GenerateUrlReport((testUrl))
