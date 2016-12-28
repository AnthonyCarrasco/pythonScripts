#! python

import webbrowser, sys, requests, bs4, pyperclip

''' A simple python script to perform a Google search '''
print('Feeling Lucky Punk????')
print('...................\n')

'''Take command line arguments and peform a google search '''
if len(sys.argv) > 1:
    response = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    response.raise_for_status()
else:
    response = requests.get('http://google.com/search?q=' + pyperclip.paste())
    response.raise_for_status()

''' Extract top results and open several tabs in browser '''
result = bs4.BeautifulSoup(response.text, "lxml")

listElement = result.select('.r a')

minimum= min(5, len(listElement))

for i in range(minimum):
    webbrowser.open('http://google.com' + listElement[i].get('href'))
