# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса 
import configuration 
# Импорт библиотеки requests для выполнения HTTP-запросов 
import requests 
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса 
import data  

def test_order_track():
    # Выполнить запрос на создание заказа.
    response_create_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.NEW_ORDER_DATA, headers=data.HEADERS)
    
    # Сохранить номер трека заказа.
    track = response_create_order.json()["track"]

    # Выполнить запрос на получения заказа по треку заказа.
    response_get_track = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t":track})

    # Проверить, что код ответа равен 200.
    assert response_get_track.status_code == 200