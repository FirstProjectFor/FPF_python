import json

data = [{'a': 'A', 'c': '3.0', 'b': (2, 4)}]

data_json = json.dumps(data)
print("json.dumps() -> {}".format(data_json))
data_load = json.loads(data_json)
print("json.loads() -> {}".format(data_load))
