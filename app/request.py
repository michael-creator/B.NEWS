
import urllib.request,json
from .models import source
from config import Config
# Getting api key
api_key = Config.NEWS_API_KEY
# Getting the news base url
base_url = Config.NEWS_API_BASE_URL

# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    get_news_url = (base_url).format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        result= getResult(get_news_response['sources'])
        return result 

def getResult(list):
    get_list=[]
    for newsitem in list:
        id = newsitem.get('id')
        name = newsitem.get('name')
        description = newsitem.get('description')
        obj = source(id,name,description)
        get_list.append(obj)
    return get_list


