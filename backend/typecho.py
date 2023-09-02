import requests
from bs4 import BeautifulSoup


def typecho_GetPageLenth(res: BeautifulSoup):
    pagenavi = BeautifulSoup(str(res.find_all(name="div", class_="pagenavi")[0]), "html.parser")
    li_tags = pagenavi.find_all("li")
    return li_tags[-2].text


def typecho_GetArticlesInfo(url: str, index: int | None):
    if not index == None:
        for i in range(1, index + 1):
            url_page = url + "page/{}/".format(i)
            res_current = BeautifulSoup(requests.get(url_page).text, "html.parser")
            articles = res_current.find_all("article")
            for i in articles:
                print(str(i.h2.text).strip())
                link = BeautifulSoup(str(i.h2), "html.parser").find_all("a", href=True)[0]["href"]
                print(link)
    else:
        for i in range(1, 1000):
            url_page = url + "page/{}/".format(i)
            res_current = BeautifulSoup(requests.get(url_page).text, "html.parser")
            articles = res_current.find_all("article")
            if articles == []:
                print("[+] 无法获取更多页面，终止")
                break
            for i in articles:
                data = i.text.replace("\r", "").split("\n")
                data = [i for i in data if i != ""]
                print(str(data[0]).strip())
                link = BeautifulSoup(str(i), "html.parser").find_all("a", href=True)[0]["href"]
                print(link)


def typecho_crawler(url: str):
    res_index = BeautifulSoup(requests.get(url).text, "html.parser")
    try:
        MaxPageLenth = int(typecho_GetPageLenth(res_index))
        typecho_GetArticlesInfo(url, MaxPageLenth)
    except:
        print("[+] 无法获取文章总数")
        typecho_GetArticlesInfo(url, None)


if __name__ == "__main__":
    url = "https://www.woshidie.com/"  # 小松博客
    # url = "https://ha1c9on.top/"  # 满秋
    if not url.endswith("/"):
        url = url + "/"
    typecho_crawler(url)
