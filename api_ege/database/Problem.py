from bs4.element import Tag

class Problem:
    symbols = {
        chr(173): "",
        chr(8239): " ",
        chr(160): " ",
        chr(8201): " "
    }

    def __init__(self, prob_view: Tag):
        answer_view = prob_view.find("div", {"class": "answer"}).text

        self.answer = answer_view[7:].split("&")

        question_view = prob_view.find("div", {"class": "pbody"})

        self.question = ""
        self.set_question(question_view.text)

        p_type, g, number = prob_view.find("span", {"class": "prob_nums"}).get_text().split(chr(160))
        self.type = int(p_type.split(" ")[1])
        self.number = int(number)

    def set_question(self, text):
        for symbol in self.symbols:
            text = text.replace(symbol, self.symbols[symbol])

        while "  " in text:
            text = text.replace("  ", " ")

        if text.endswith("Ответ: "):
            self.question = text[:-7]
        else:
            self.question = text

        return self.question
