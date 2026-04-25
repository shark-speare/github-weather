from service.fetch import fetch
from service.location import Location
from service.render import format_article

cities = [
    "臺北市",
    "新北市",
    "桃園市",
    "新竹縣",
    "新竹市",
    "苗栗縣",
    "臺中市",
    "彰化縣",
    "雲林縣",
    "嘉義縣",
    "嘉義市",
    "臺南市",
    "高雄市",
    "屏東縣",
    "臺東縣",
    "花蓮縣",
    "宜蘭縣",
    "基隆市",
    "澎湖縣",
    "金門縣",
    "連江縣"
]

def make_file(city:str): ...

def main():
    for city in cities:
        data = fetch(city)
        loc = Location.from_dict(data)
        result = format_article(loc)

        with open(f"./weather/{city}.md", mode="w", encoding="utf8") as f:
            f.write(result)


if __name__ == "__main__":
    main()
