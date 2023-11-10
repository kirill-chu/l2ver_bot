import logging

from exceptions import ItemLimitError, ItemTypeError, ItemsTypeError


def chek_list(data):
    result = None
    logging.info(f'Поступили данные на проверку {data}')
    if not (isinstance(data, list)):
        err_msg('Переданные данные не являются списком.')
        logging.error(err_msg, stack_info=True)
        raise ItemsTypeError(err_msg)

    if not all([str(i).isdigit() for i in data]):
        err_msg = ('Последовательность может состоять только и из целых '
                   'чисел больше 0 и меньше 100')
        logging.error(err_msg, stack_info=True)
        raise ItemTypeError(err_msg)
    result = list(map(int, data))
    logging.info(f'Преобразованные данные {result}')
    if min(result) <= 0:
        err_msg = 'Значение не может быть меньше или равно 0.'
        logging.error(err_msg, stack_info=True)
        raise ItemLimitError(err_msg)
    if max(result) > 100:
        err_msg = 'Значение не может быть больше 100.'
        logging.error(err_msg, stack_info=True)
        raise ItemLimitError(err_msg)
    return result



def multiple(data):
    result = 1
    for x in data:
        result *= x
    return result
