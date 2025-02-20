
# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса 
import configuration 
# Импорт библиотеки requests для выполнения HTTP-запросов 
import requests 
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса 
import data

def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.NEW_ORDER_DATA, headers=data.HEADERS)

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t":track})
