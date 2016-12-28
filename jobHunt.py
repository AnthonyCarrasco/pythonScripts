import webbrowser, sys , pyperclip

''' Simple script to pull up all latest job postings from indeed'''
cities = ['New+York', 'Connecticut', 'Danbury', 'Boston']

for city in cities:
    webbrowser.open('https://indeed.com/jobs?q=computer+science&l=' + city + '&fromage=last')
