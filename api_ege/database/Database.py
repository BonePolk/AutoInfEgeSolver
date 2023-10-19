import sqlite3
from api_ege.database.Problem import Problem

class Database:

    def __init__(self):
        self.db = sqlite3.connect('problems.db')
        self.cursor = self.db.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY,
                text TEXT NOT NULL,
                answers TEXT NOT NULL,
                type INTEGER
            )
        ''')

        self.db.commit()

    def add_problem(self, problem: Problem):
        self.cursor.execute(f'''
            INSERT or IGNORE INTO problems VALUES ({problem.number} ,"{problem.question}", "{"&".join(problem.answer)}", {problem.type});
        ''')

        self.db.commit()

    def get_problem_answer(self, text):
        self.cursor.execute(f'SELECT answers FROM problems WHERE text="{text}"')

        fetched = self.cursor.fetchone()
        return fetched[0].split("&") if fetched is not None else None

    def close(self):
        self.db.close()
