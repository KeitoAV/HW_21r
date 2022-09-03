from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import InvalidRequest, BaseError, InvalidStorageName

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "ёлка": 25,
    "торт": 5,
    "мороженое": 5,
    "зефир": 5

})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2

})

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!')

    while True:
        # TODO: Ввести все товары во всех хранилищах
        for storage_name in storages:
            print(f'\nСейчас в {storage_name}:\n {storages[storage_name].get_items()}')
            print(f'Свободного места в {storage_name}: {storages[storage_name].get_free_space()}')

        # TODO: Забрать у пользователя строку с запросом
        print('\nПример ввода запроса == Доставить 1 собачка из склад в магазин ==')
        print('Чтобы завершить работу введите "стоп" или "stop"')
        user_input = input('\nВведите запрос: ')

        if user_input in ('stop', 'стоп'):
            break

        # TODO: Создать класс запроса

        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStorageName) as error:
            print(error.message)
            continue

        # TODO: Обработать доставку, если запрос валидный
        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
