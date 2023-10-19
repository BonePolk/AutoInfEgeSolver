from api_ege.Task import Task
from api_ege.database.Parser import Parser


class Solver:
    def __init__(self, problem: Task):
        parser = Parser()
        self.answer = parser.get_answer_from_db(problem.task_text)

        if self.answer is None:
            print(f"problem not in database start re-parsing type {problem.type}")
            parser.parse_themes()
            for theme in parser.themes[problem.type]:
                parser.parse_theme(theme)

        self.answer = parser.get_answer_from_db(problem.task_text)

        if self.answer is None:
            print(f"problem with {problem.task_text} not solved")

    def __repr__(self):
        return "&".join(self.answer)
