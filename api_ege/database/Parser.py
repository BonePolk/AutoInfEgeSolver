import requests
from bs4 import BeautifulSoup
from api_ege.database.Theme import Theme
from api_ege.database.Problem import Problem
from api_ege.database.Database import Database


class Parser:
    themes = {
    }

    def __init__(self):
        self.themes = {
        }
        self.db = Database()

    def parse_themes(self):
        if self.themes:
            return

        json = requests.get("https://inf-ege.sdamgia.ru/newapi/general").json()
        for topic in json["constructor"]:
            if topic["num"] == "extra":
                continue

            if topic["subtopics"]:
                topic_type = int(topic["num"])
                for subtopic in topic["subtopics"]:
                    self._add_theme(topic_type, int(subtopic["id"]), int(subtopic["amount"]))
            else:
                self._add_theme(int(topic["num"]), int(topic["id"]), int(topic["amount"]))

    def _add_theme(self, theme_type, theme_id, amount):
        if theme_type not in self.themes:
            self.themes[theme_type] = [Theme(theme_id, amount)]
        else:
            self.themes[theme_type].append(Theme(theme_id, amount))

    def parse_theme(self, theme):
        html = requests.get(f"https://inf-ege.sdamgia.ru/test?theme={theme.id}&print=true").content
        soup = BeautifulSoup(html, "html.parser")

        for problem in soup.find_all("div", {"class": "prob_maindiv"}):
            prob = Problem(problem)
            self.db.add_problem(prob)

            self.parse_minor_problems(prob.number)

    def get_answer_from_db(self, text):
        return self.db.get_problem_answer(text)

    def parse_minor_problems(self, problem_id):
        html = requests.get(f"https://inf-ege.sdamgia.ru/problem?id={problem_id}").content
        soup = BeautifulSoup(html, "html.parser")

        minors = soup.find("div", {"class": "minor", "style": "clear:both;margin-bottom:15px;"}).text
        if minors:
            minors = minors.split(":")[1].split(" ")[1:-1]
            for minor_id in minors:
                self.parse_one_problem(minor_id)

    def parse_one_problem(self, problem_id):
        html = requests.get(f"https://inf-ege.sdamgia.ru/problem?id={problem_id}&print=true").content
        soup = BeautifulSoup(html.decode('utf-8', 'ignore'), "html.parser")

        self.db.add_problem(Problem(soup.find("div", {"class": "prob_maindiv"})))
