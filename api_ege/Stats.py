import requests
from bs4 import BeautifulSoup

class Stats:
    def __init__(self, headers):
        self.headers = headers
        self.homework_tests = []

    def parse_homework(self):
        html = requests.get("https://inf-ege.sdamgia.ru/user_stat", headers=self.headers).content
        soup = BeautifulSoup(html, "html.parser")

        for homework_view in soup.find_all("div", {"class": "assigned_testn"}):
            self.homework_tests.append(int(homework_view.find("a").text))
