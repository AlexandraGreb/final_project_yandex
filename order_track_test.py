# Гребенщикова Александра, 26-я когорта - Финальный проект. Инженер по тестированию плюс
import common

def positive_assert(response):
    assert response.status_code == 200

def test_order_track():
    # Выполнить запрос на создание заказа.
    response_create_order = common.create_order()
    
    # Сохранить номер трека заказа.
    track = response_create_order.json()["track"]

    # Выполнить запрос на получения заказа по треку заказа.
    response_get_track = common.get_order_by_track(track)

    # Проверить, что код ответа равен 200.
    positive_assert(response_get_track)