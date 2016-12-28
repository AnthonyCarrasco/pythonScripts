#! python
''' mapScript takes an address and searches using Google Maps '''

import webbrowser, sys , pyperclip

#command line argument
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
#else take address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
