import requests, my_setting

api_key = my_setting.MOVIE_API_KEY

def movies_search(title):

    url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?'
    params = {
        'collection' : 'kmdb_new2',
        'detail' : 'Y',
        'title': title,
        'ServiceKey': api_key,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        movies_data = response.json()['Data'][0]['Result']
        return movies_data
    else:
        return None
    
