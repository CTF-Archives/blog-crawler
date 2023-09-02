from bs4 import BeautifulSoup

# 假设 html 是包含上述 HTML 数据的字符串
html = '''
<div class="pagenavi">
    <li class="current"><a href="https://www.woshidie.com/page/1/">1</a></li>
    <li><a href="https://www.woshidie.com/page/2/">2</a></li>
    <li><a href="https://www.woshidie.com/page/3/">3</a></li>
    <li><span>...</span></li>
    <li><a href="https://www.woshidie.com/page/10/">10</a></li>
    <li class="next"><a href="https://www.woshidie.com/page/2/">后一页 »</a></li>
</div>
'''

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html, 'html.parser')

# 查找所有的 <li> 节点
li_tags = soup.find_all('li')

# 遍历节点并进行处理
for li in li_tags:
    print(li.text)