from fastapi import APIRouter
import base64
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

router = APIRouter()
host = 'https://www.azlyrics.com'


@router.get('/lyrics/{id}')
def get_lyrics(id):
    # decode the id
    url = base64.b64decode(id)
    url = url.decode('utf8')

    # geting the text
    lyricsurl = host + url
    res = requests.get(lyricsurl)
    html = BeautifulSoup(res.text, features='html.parser')
    css = 'div.col-xs-12.col-lg-8.text-center > div:nth-of-type(5)'
    lyric = html.select_one(css).text
    return {'lyric': lyric}
