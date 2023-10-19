import requests
from bs4 import BeautifulSoup
from api_ege.Task import Task
from api_ege.database.Solver import Solver


class Test:

    def __init__(self, headers, test_id):
        self.headers = headers
        self.test_id = test_id

        self.continue_id = 0
        self.soup = None
        self.get_continue()

        self.tasks = []
        self.hash = ""
        self.get_hash()

        self.answers = []

    def get_continue(self):
        requests.get(f"https://inf-ege.sdamgia.ru/test?id={self.test_id}", headers=self.headers)
        html = requests.get(f"https://inf-ege.sdamgia.ru/test?id={self.test_id}", headers=self.headers).text

        self.soup = BeautifulSoup(html, "html.parser")

        self.continue_id = int(self.soup.find("a", {"class": "a_btn"})["href"].split("&")[1].split("=")[1])

        return self.continue_id

    def continue_test(self):
        html = requests.get(f"https://inf-ege.sdamgia.ru/test?id={self.test_id}&continue={self.continue_id}&rtid=0",
                            headers=self.headers).content

        soup = BeautifulSoup(html, "html.parser")

        for html_task in soup.find_all("div", {"class": "prob_view"}):
            self.tasks.append(Task(html_task))

    def get_hash(self):
        self.hash = self.soup.find("input", {"name": "hash"})["value"]

    def solve_tasks(self):
        for task in self.tasks:
            solver = Solver(task)
            self.answers.append(solver.answer)

    def __repr__(self):
        return f'''{"{"}headers={self.headers} test_id={self.test_id} continue_id={self.continue_id} tasks={self.tasks}{"}"}'''
