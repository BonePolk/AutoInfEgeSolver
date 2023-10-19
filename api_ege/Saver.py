import requests
from api_ege.Task import Task
from api_ege.Test import Test

class Saver:
    def __init__(self, headers, continue_id):
        self.headers = headers
        self.continue_id = continue_id

    def _save_part(self, btn_name, answer):
        data = {
            "stat_id": f"{self.continue_id}",
            "name": btn_name,
            "answer[]": answer
        }

        status = requests.post("https://inf-ege.sdamgia.ru/test?a=save_part&ajax=1", headers=self.headers,
                               data=data).text

        return status[:2] == "ok"

    def _save_full(self, answer_name, answers):
        data = {
            "stat_id": f"{self.continue_id}",
            "name": answer_name,
            "answer[]": answers
        }
    
        status = requests.post("https://inf-ege.sdamgia.ru/test?a=save_part&ajax=1", headers=self.headers,
                               data=data).text

        return status[:2] == "ok"

    def save_part(self, task: Task, answers):
        answer_name = "_".join(task.btns[0].name.split("_")[:-1])
        return self._save_full(answer_name, answers) and self._save_part(task.btns[0].name, answers[0])

    def send_answers(self, test: Test):
        data = {
            "is_cr": 1,
            "hash": test.hash,
            "stat_id": test.continue_id,
            "timer": 120930,
            "a": "check",
            "test_id": test.test_id
        }

        for i, answer in enumerate(test.answers):
            task = test.tasks[i]
            for ib, num in enumerate(answer):
                data[task.btns[ib].name] = num

        status = requests.get("https://inf-ege.sdamgia.ru/test", headers=self.headers, data=data).status_code

        return status == 302


