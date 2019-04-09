import requests
from bs4 import BeautifulSoup
from util import print_util

# 主机地址
host = "http://www.sunfeilong.cn"
res = requests.request("GET", host)
print_util.print_key_value("状态码", res.status_code)
print_util.print_key_value("content-type", res.headers['content-type'])

# 设置编码格式
res.encoding = requests.utils.get_encodings_from_content(res.text)

# bs4 解析 HTML
page = BeautifulSoup(res.text, 'html.parser')

print_util.print_key_value("标题", page.title.text)
print_util.print_key_value("id=bloggerContext", page.find(id="bloggerContext"))
print_util.print_key_value("id=bloggerContext 的 class", page.find(id="bloggerContext")['class'])
print_util.print_key_value("title 的文本", page.find("title").text)

# 查找所有
count = 0
for li in page.find_all(name="link"):
    count = count + 1
    print_util.print_key_value("引用的标签" + str(count), host + str(li.get("href")).replace("..", ""))

# 打印所有文本
for line in page.get_text().strip().split("\n"):
    if len(line.strip()) > 0:
        print_util.print_key_value("文本内容", line.strip())
