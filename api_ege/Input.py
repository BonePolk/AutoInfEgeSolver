class Input:
    value = ""
    name = ""

    def __init__(self, task_line):
        self.name = task_line["name"]
        self.value = 0

    def __repr__(self):
        return f'{self.name}'