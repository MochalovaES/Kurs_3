import datetime
from datetime import datetime
from utils.functions import load_is_executed, load_sorted_operations, print_operations


def test_load_is_executed():
    operations = [{'id': 441945886,
                   'state': 'EXECUTED',
                   'date': '2019-08-26T10:50:58.294041',
                   'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                   'description': 'Перевод организации',
                   'from': 'Maestro 1596837868705199',
                   'to': 'Счет 64686473678894779589'
                   }]
    executed_operations = [{'id': 441945886,
                            'state': 'EXECUTED',
                            'date': '2019-08-26T10:50:58.294041',
                            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'from': 'Maestro 1596837868705199',
                            'to': 'Счет 64686473678894779589'
                            }]
    assert load_is_executed(operations) == executed_operations


def test_load_sorted_operations():
    executed_operations = [{'id': 441945886,
                           'state': 'EXECUTED',
                            'date': '2019-08-26T10:50:58.294041',
                            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'from': 'Maestro 1596837868705199',
                            'to': 'Счет 64686473678894779589'
                            }]
    sorted_operations = [{'date': datetime(2019, 8, 26, 0, 0),
                         'description': 'Перевод организации',
                          'from': 'Maestro 1596 83** **** 5199',
                          'to': 'Счет **9589',
                          'amount': '31957.58',
                          'code': 'руб.'}]
    assert load_sorted_operations(executed_operations) == sorted_operations

    executed_operations = [{'id': 441945886,
                            'state': 'EXECUTED',
                            'date': '2019-08-26T10:50:58.294041',
                            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'from': 'Счет 64686473678894779589',
                            'to': 'Счет 64686473678894779589'
                            }]
    sorted_operations = [{'date': datetime(2019, 8, 26, 0, 0),
                          'description': 'Перевод организации',
                          'from': 'Счет **9589',
                          'to': 'Счет **9589',
                          'amount': '31957.58',
                          'code': 'руб.'}]
    assert load_sorted_operations(executed_operations) == sorted_operations

    executed_operations = [{'id': 441945886,
                            'state': 'EXECUTED',
                            'date': '2019-08-26T10:50:58.294041',
                            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'to': 'Счет 64686473678894779589'
                            }]
    sorted_operations = [{'date': datetime(2019, 8, 26, 0, 0),
                          'description': 'Перевод организации',
                          'from': 'Наличные средства',
                          'to': 'Счет **9589',
                          'amount': '31957.58',
                          'code': 'руб.'}]
    assert load_sorted_operations(executed_operations) == sorted_operations


def test_print_operations():
    sorted_operations = [{'date': datetime(2019, 8, 26, 0, 0),
                          'description': 'Перевод организации',
                          'from': 'Maestro 1596 83** **** 5199',
                          'to': 'Счет **9589',
                          'amount': '31957.58',
                          'code': 'руб.'}]
    str_print_operations = ('26.08.2019 Перевод организации\n'
                            'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                            '31957.58  руб.\n'
                            '\n')
    assert print_operations(sorted_operations) == str_print_operations
