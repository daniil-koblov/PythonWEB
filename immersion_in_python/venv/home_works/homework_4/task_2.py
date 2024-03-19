#  Решение

def key_params(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        try:
            hash(v)
            my_dict[v] = k
        except TypeError:
            my_dict[str(v)] = k
    return my_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
#  Эталонное решение


# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if value is None:
#             result[value] = key
#         elif isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result
