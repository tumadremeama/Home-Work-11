def introspection_info(obj):
    """
    Получает информачию об обекте с помощью интроспекции.

    Args:
        obj: для которого нужо получить информацию

    Returns:
        dict: словарь с информацией об объекте.
    """
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir (obj) if callable(getattr(obj, method))]
    }
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = 'builtins'
        
    if isinstance(obj, (int, float, complex)):
        info['value'] = obj
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif hasattr(obj, '__len__'):
        info['length'] = len(obj)

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Hello, Wrold!')
print(string_info)

list_info = introspection_info([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list_info)