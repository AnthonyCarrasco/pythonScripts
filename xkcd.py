#! python3
import os, requests, bs4

''' simple script to download xkcd comics '''

url = 'http://xkcd.com'
os.makedirs('../xkcd', exist_ok=True)

while not url.endswith('#'):
    response = requests.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "lxml")

    comic = soup.select('#comic img')

    if comic == []:
        print("URL not found")
    else:
        comicUrl = comic[0].get('src')
        print(comicUrl)
        response = requests.get('http:'+ comicUrl)
        response.raise_for_status()

        imageFile = open(os.path.join('../xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in response.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
