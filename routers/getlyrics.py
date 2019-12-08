from fastapi import APIRouter
import base64
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

router = APIRouter()
host = 'https://www.azlyrics.com'


@router.get('/lyrics/{id}')
async def get_lyrics(id):
    # decode the id
    url = base64.b64decode(id)
    url = url.decode('utf8')
    print('url', url)
    # geting the text
    lyricsurl = host + url
    res = await requests.get(lyricsurl)
    html = await BeautifulSoup(res.text, features='html.parser')
    print(html.text)
    css = 'div.col-xs-12.col-lg-8.text-center > div:nth-of-type(5)'
    try:
        lyric = await html.select_one(css).text
    except:
        lyric = 'lyrics not found'
    print(lyric)
    return {'lyric': lyric}
