class ItemLimitError(Exception):
    """
    Вызывается, когда значение в последовательности меньше или равно 0 или
    больше или равно 100
    """


class ItemTypeError(Exception):
    """
    Вызывается, элемент в списке не определенного типа.
    """


class ItemsTypeError(Exception):
    """
    Вызывается, когда данные не являются списком.
    """
