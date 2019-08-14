"""
A Python script for parsing all the links from a Discord server
that has been converted into an HTML page, using a tool such as
Discord Chat Exporter. 

The script collects all the links from the page together into
a text file, and that text file is saved to the location of the
script on the user's machine. 

For example, if the script is stored in the folder "C:\Documents\cmd_tool"
then this is also where the text file will be saved.
"""

import re
import requests
import sys
import urllib.request
from bs4 import BeautifulSoup

"""
For parsing URLs
def parse_url():
    url = sys.argv[0]
    "https://big-sexy-pregnant-belly.tumblr.com/"
    parseUrl = urllib.request.urlopen(url)
    URLsoup = BeautifulSoup(parseUrl, 'html.parser')
"""

# For parsing locally stored files
def parse_local():
    # Links must be in the form: <driveletter>/<filename.html>
    local = sys.argv[1]
    file = open(local, encoding="mbcs")
    soup = BeautifulSoup(file, 'html.parser')

    links = [div.find('a')['href'] for div in soup.find_all("div", {"class" : "chatlog__attachment"})]
    
    """
    Write the output of the program into a text file.
    If the file does not exist, create it.
    """
    f = open('output2.txt', 'a+')
    f.write('\n'.join(links))

# The main method of the program 
def main(): 
    """
    if linkType == 'URL':
        parseURL()
    else: 
    """
    parse_local()

# To call the main function
if __name__ == "__main__":
    main()