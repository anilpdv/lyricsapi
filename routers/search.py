from fastapi import APIRouter
import base64
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

router = APIRouter()


@router.get('/')
async def home():
    return {'msg': 'welcome to lyrics api', 'credits': 'powered by fastapi', 'open-api': 'some url', 'redoc': 'some url'}


@router.get('/search')
async def search_lyrics(q: str, p: str = '1'):
    url: str = "https://search.azlyrics.com/search.php"
    url = url + '?q=' + q + '&w=songs' + '&p='+p
    lyrics = []

    # getting the response
    res = requests.get(url)

    # loading res.text in to beautiful soup
    html = BeautifulSoup(res.text, features='html.parser')
    lyrics_list = html.select('.text-left.visitedlyr')

    for l in lyrics_list:
        lyric = {}
        link = l.a['href']
        parsedurl = urlparse(link)
        link = parsedurl.path
        encoded = base64.b64encode(link.encode())
        lyric['id'] = encoded.decode('utf8')
        lyric['song'] = l.a.text
        lyric['author'] = l.find_all('b')[1].text
        lyrics.append(lyric)

    return {'results': lyrics}
