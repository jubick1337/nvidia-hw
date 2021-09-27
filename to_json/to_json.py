def to_json(func):
    output = func()
    res = "{"
    for key, value in output.items():
        res += f'"{key}": {value}, '
    res = res[:-2]
    res += "}"
    return res
