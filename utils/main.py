import json


def open_json():
    """
    Читаем json-файл
    :return:
    """
    with open('../operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def number_encryption(number_account):
    """
    Прячем часть символов в счетах и картах
    :param number_account:
    :return: возвращаем номер счета или карты, взависимости от карты или счета
    """
    if 'Счет' in number_account:
        return "Счет **" + number_account[-4:]
    elif 'Maestro' in number_account:
        return number_account[:12] + " " + number_account[12:14] + "** **** " + number_account[-4:]
    elif 'Visa' in number_account:
        return number_account[:17] + " " + number_account[17:19] + "** **** " + number_account[-4:]
    elif 'MasterCard' in number_account:
        return number_account[:15] + " " + number_account[17:19] + "** **** " + number_account[-4:]


def formate_date(date):
    """
    Форматируем дату к виду DD.MM.YYYY
    :param date:
    :return: Возвращаем отформатированный формат
    """
    return ".".join(date.split('T')[0].split('-')[::-1])


def print_operation():
    """
    Сортируем данные по state и date и выводим данные
    """
    operation_list = open_json()
    operation_list = filter(lambda x:x.get('state')=='EXECUTED', operation_list)
    operation_list = sorted(operation_list, key=lambda x:x.get('date'), reverse=True)

    for stroke in list(operation_list)[:5]:
            if stroke.get("from"):
                print(f'{formate_date(stroke["date"])} {stroke["description"]}\n'
                      f'{number_encryption(stroke["from"])} -> {number_encryption(stroke["to"])}\n'
                      f'{stroke["operationAmount"]["amount"]} {stroke["operationAmount"]["currency"]["name"]}\n')
            else:
                print(f'{formate_date(stroke["date"])} {stroke["description"]}\n'
                      f'{number_encryption(stroke["to"])}\n'
                      f'{stroke["operationAmount"]["amount"]} {stroke["operationAmount"]["currency"]["name"]}\n')


if __name__ == "__main__":
    print_operation()
