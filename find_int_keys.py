def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    list = []
    for i in data.keys():
        if i.isdigit():
            list.append(i)
    return list
print(find_int_keys({'a': 1, 3 : 2, 'c': 3, 10:'a'}))