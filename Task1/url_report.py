import re
import string
import sys
import urllib
from bs4 import BeautifulSoup

__author__ = 'Omar Salman'

# TODO: Can you please inherit this from "object"
# Done: Now inherits from the base object class
class UrlReport(object):
    def __init__(self, url):
        self.url = url
        self.helper = UrlHelper()
        self.html = self.helper.get_html(url)
        self.soup = ''
        self.soup_text = ''

    def is_valid(self):
        if not self.html:
            return False
        return True

    def reset_url(self, url):
        self.url = url
        self.html = self.helper.get_html(url)
        self.soup = ''
        self.soup_text = ''

    def get_content_size(self):
        # TODO: You don't have to check for "self.html" in every function. because if there is no self.html
        # these functions will not be called ever. is_valid() function will quit the program already.
        # Done: Removed this unnecessary check from each of the functions that contained it. Thanks for raising
        # this point because I realized that there was too much redundancy.
        if not self.soup_text:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        return len(self.soup_text)

    def get_word_count(self):
        # TODO: Same, no need to check here
        # Done: For this and the rest
        if not self.soup_text:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        text = self.helper.format_text(self.soup_text)
        return len(re.findall('\w+', text))

    def get_unique_word_count(self):
        # TODO: Also, we don't usually leave a white space below the function in python.
        # Done: Removal of unnecessary whitespace after function definition
        if not self.soup_text:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        text = self.helper.format_text(self.soup_text)
        return len(set(re.findall('\w+', text.lower().encode('utf-8'))))

    def get_alphabet_count(self):
        if not self.soup_text:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        # TODO: Variable names should be more readable. "c" is not a proper name
        # Done: c changed to character to make things for readable
        return len([character for character in self.soup_text if character in string.ascii_letters])

    def meta_tag_count(self):
        if not self.soup:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        return len(self.soup.find_all('meta'))

    def get_five_most_frequent_words(self):
        if not self.soup_text:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        # Nice :)
        # Thanks
        words = re.findall('\w+', self.soup_text.lower().encode('utf-8'))
        words_dict = {}

        for each in words:
            words_dict[each] = words_dict.get(each, 0) + 1

        words = sorted(words_dict.keys(), key=words_dict.get, reverse=True)
        # Awesome..
        # Thanks
        top_five = words[:5]
        return ', '.join(top_five)

    def get_anchor_tag_count(self):
        if not self.soup:
            self.soup, self.soup_text = self.helper.initialize_beautiful_soup(self.html)
        return len(self.soup.find_all('a'))


class UrlHelper(object):
    def get_html(self, url):
        try:
            html = urllib.urlopen(url).read()
            return html
        except:
            print "The url given is not valid"
            return ''

    # TODO: We should move these functions in a separate class if they don't belong to above class.
    # Done: Created a separate class
    def initialize_beautiful_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        all_text = soup.get_text()
        return (soup, all_text)

    def format_text(self, text):
        text = re.sub('\s+', ' ', text).strip()
        text = "".join(character for character in text if character not in ('!','.',':',',',))
        return text


def main(url):
    report = UrlReport(url)
    # TODO: Since we are already checking and validating the "url" in this function. 
    # no need to make the html check in every other function. Below condition will prevent the other codes to run.
    # Done: Good point made here
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
