import json
from backend import typecho


def typecho_main():
    with open("./source/typecho.json", "r") as f:
        persons = json.load(f)["blog"]
    for person in persons:
        name = person["name"]
        url = person["url"]
        print(name)
        typecho.typecho_crawler(url)


if __name__ == "__main__":
    typecho_main()
