# Гребенщикова Александра, 26-я когорта - Финальный проект. Инженер по тестированию плюс

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

def positive_assert(response):
    assert response.status_code == 200

def test_order_track():
    # Выполнить запрос на создание заказа.
    response_create_order = create_order()
    
    # Сохранить номер трека заказа.
    track = response_create_order.json()["track"]

    # Выполнить запрос на получения заказа по треку заказа.
    response_get_track = get_order_by_track(track)

    # Проверить, что код ответа равен 200.
    positive_assert(response_get_track)