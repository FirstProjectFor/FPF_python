import requests
from bs4 import BeautifulSoup

# 主机地址
host = "http://www.sunfeilong.cn"

res = requests.request("GET", host)
print(res.status_code)
print(res.headers['content-type'])
# 设置编码格式
res.encoding = requests.utils.get_encodings_from_content(res.text)

# bs4 解析 HTML
page = BeautifulSoup(res.text, 'html.parser')

# title 标签
print(page.title)
# 对应的id的标签
print(page.find(id="bloggerContext"))
# 标签的样式
print(page.find(id="bloggerContext")['class'])
# bio
print(page.find(id="bloggerContext").text)
print(page.find("title").text)
# 查找所有
for li in page.find_all(name="link"):
    print(host + str(li.get("href")).replace("..", ""))

# 打印所有文本
for line in page.get_text().strip().split("\n"):
    if len(line.strip()) > 0:
        print(line.strip())

