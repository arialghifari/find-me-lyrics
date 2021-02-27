import requests
from bs4 import BeautifulSoup

def lyrics(key):
  url = f"https://www.google.com/search?q={key}+lyrics&ie=UTF-8"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
  source = requests.get(url, headers=headers)
  
  soup = BeautifulSoup(source.text, "html.parser")

  lyricsRef = soup.find("div", {"class":"hwc"})
  titleRef = soup.find("div", {"class":"kCrYT"})

  if lyricsRef is None or titleRef is None:
    return None
  else:
    return titleRef.text, lyricsRef.text

if __name__ == '__main__':
  result = lyrics("Hello")
  if result is None:
    print('Sorry We Cannot Find The Lyrics')
  else:
    print("Song Title : ")
    print(result[0].replace("/", "by"))
    print("")
    print("Lyrics :")
    print(result[1])


