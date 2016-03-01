from bs4 import BeautifulSoup
import urllib
import re
import string

__author__ = 'Omar Salman'

def GenerateUrlReport(url):

    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    sizeAllContent = len(text)
    text = re.sub('\s+', ' ', text).strip()
    text = "".join(c for c in text if c not in ('!','.',':',',',))

    totalWordCount = len(re.findall('\w+', text))
    uniqueWordCount = len(set(re.findall('\w+', text.lower().encode('utf-8'))))
    alphabetCount = len([c for c in text if c in string.ascii_letters])
    metaTagCount = len(soup.find_all('meta'))

    words = re.findall('\w+', text.lower().encode('utf-8'))
    print words

    words_dict = {}

    for each in words:
        words_dict[each] = words_dict.get(each, 0) + 1

    words = sorted(words_dict.keys(), key=words_dict.get)
    words.reverse()

    topFiveFrequencyWords = words[:5]
    totalAnchorTags = len(soup.find_all('a'))

    fout = open('Report.txt', 'w')
    fout.write('Report for Url : ' + url)
    fout.write('\n\n')
    fout.write('Total Count of words: ' + str(totalWordCount) + '\n')
    fout.write('Total Count of unique words: ' + str(uniqueWordCount) + '\n')
    fout.write('Total Size of content: ' + str(sizeAllContent) + '\n')
    fout.write('Total Count of alphabets: ' + str(alphabetCount) + '\n')
    fout.write('Total Count of meta tags: ' + str(metaTagCount) + '\n')
    fout.write('Top 5 most frequent words: ' + ', '.join(topFiveFrequencyWords) + '\n')
    fout.write('Total Count of anchor tags: ' + str(totalAnchorTags) + '\n')
    fout.close()



#######################################################################################################################
testUrl = 'http://www.yahoo.com'
GenerateUrlReport((testUrl))