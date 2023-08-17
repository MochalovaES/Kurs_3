import json
import datetime
from datetime import datetime


def load_operations(filename):
    """
    Функция вытаскивает все операции из файла 'operations.json'
    :return: список всех проведенных операций пользователем
    """

    with open(filename, 'r', encoding='utf-8') as f:
        operations = json.load(f)
    return operations


def load_is_executed(operations):
    """
    Функция переберает список и вытаскивает операции с данными "EXECUTED"  — выполнена
    :return: список выполненных операций
    """

    executed_operations = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def load_sorted_operations(executed_operations):
    """
    Функция переберает список по ключам, создает список необходимых значений,
    сортирует операции по дате и выводит последние пять
    :return: пять последних операций
    """

    list_operations = []
    for item in executed_operations:
        if 'from' in item:
            if 'Счет' in item['from']:
                item_from = 'Счет **' + item['from'][-4:]
            else:
                item_from = item['from'][0:-12] + ' ' + item['from'][-12:-10] + '** **** ' + item['from'][-4:]
        else:
            item_from = 'Наличные средства'
        item_date = item['date'][8:10] + '.' + item['date'][5:7] + '.' + item['date'][0:4]
        item_date_obj = datetime.strptime(item_date, '%d.%m.%Y')
        item_to = 'Счет **' + item['to'][-4:]
        dict_operations = {'date': item_date_obj,
                           'description': item['description'],
                           'from': item_from,
                           'to': item_to,
                           'amount': item['operationAmount']['amount'],
                           'code': item['operationAmount']['currency']['name']
                           }
        list_operations.append(dict_operations)
    sorted_operations = sorted(list_operations, key=lambda i: item['date'], reverse=True)[:5]
    return sorted_operations


def print_operations(sorted_operations):
    """
    Функция выводит на печать необходимый набор текста
    :return: печать операций
    """

    str_print_operations = ''
    for item in sorted_operations:
        str_print_operations += item['date'].strftime("%d.%m.%Y") + ' ' + item['description'] + '\n' +\
                                item['from'] + ' -> ' + item['to'] + '\n' +\
                                item['amount'] + ' ' + ' ' + item['code'] + '\n\n'

    return str_print_operations
