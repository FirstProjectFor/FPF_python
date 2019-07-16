import requests
import json

file = "D:\\Untitled-1.txt"

result = []
try:
    with open(file, 'r', encoding='utf-8') as temp:
        for line in temp.readlines():
            start = line.index('{')
            end = len(line)
            result.append(line[start:end])
except IOError as e:
    print(e)

print('number:' + str(len(result)))

url = 'http://www.baidu.com/'
for j in result:
    data = json.loads(j, encoding='utf-8')
    response = requests.post(url, data)
    print(response.ok)
    print(response.text)
