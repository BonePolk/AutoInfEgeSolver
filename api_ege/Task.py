from bs4.element import Tag
from api_ege.Input import Input


class Task:
    symbols = {
        chr(173): "",
        chr(8239): " ",
        chr(160): " ",
        chr(8201): " "
    }

    def __init__(self, html_task: Tag):
        text_div = html_task.find("div", {"class": "prob_maindiv"})

        self.number = int(text_div["data-num"])
        self.task_text = ""
        self.set_task_text(text_div.find("div", {"class": "pbody"}).getText())
        self.body_id = int(text_div["data-id"])
        self.btns = []

        for inp in html_task.find_all("input", {"class": "test_inp"}):
            self.btns.append(Input(inp))

        self.type = int(text_div.find("span", {"class": "prob_nums"}).text.split(chr(160))[0][4:])

    def set_task_text(self, text):
        for symbol in self.symbols:
            text = text.replace(symbol, self.symbols[symbol])

        while "  " in text:
            text = text.replace("  ", " ")

        if text.endswith("Ответ: "):
            self.task_text = text[:-7]
        else:
            self.task_text = text

        return self.task_text

    def __repr__(self):
        return f'''{"{"}number={self.number} type={self.type} text={self.task_text} body_id={self.body_id} btns={self.btns}{"}"}'''
