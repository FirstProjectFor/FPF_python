import io
import json

data = [{'a': 'A', 'c': '3.0', 'b': (2, 4)}]

repr_data = repr(data)
print('repr_data: {}'.format(data))
eval_data = eval(repr_data)
print('eval_data: {}'.format(eval_data))

encoded_data = json.dumps(data)
print('encoded: {}'.format(encoded_data))

decoded_data = json.loads(encoded_data)
print('decoded: {}'.format(decoded_data))

encoded_data = json.dumps(data, sort_keys=True)
print('sort keys encoded: {}'.format(encoded_data))

encoded_data = json.dumps(data, sort_keys=True, indent=4)
print('sort keys and indent encoded: {}'.format(encoded_data))

# 默认分割符是 `, ` 和 `: `
encoded_data = json.dumps(data, separators=(',', ':'))
print('encoded with separators(no bank): {}'.format(encoded_data))

data = [{'a': 'A', 'c': '3.0', (2, 4): 'b'}]

# 当 key 不为string时会抛出 TypeError, 可以设置 `skip_keys` 跳过。
try:
    json.dumps(data, skipkeys=True)
except TypeError as e:
    print(e)


class MyObj:
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return '<MyObj({})>'.format(self.s)


def convert_to_builtin_type(obj):
    print('default({})'.format(repr(obj)))
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__
    }
    d.update(obj.__dict__)
    return d


my_obj = MyObj("Test")

encode_object = json.dumps(my_obj, default=convert_to_builtin_type)
print('encode_object: {}'.format(encode_object))

# io 测试
data = [2 * int(number) for number in range(1)]

str_io = io.StringIO()
json.dump(data, str_io)

print(data)
