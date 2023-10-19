from api_ege import headers, Test, Saver, Stats
from api_ege.database.Solver import Solver
from time import sleep


def testik_test():
    testik = Test.Test(headers, 14083278)
    testik.continue_test()

    for task in testik.tasks:
        solver = Solver(task)
        saver = Saver.Saver(headers, testik.continue_id)
        print(saver.save_part(task, solver.answer))


def test_stats():
    print("checking stats")
    stats = Stats.Stats(headers)
    stats.parse_homework()

    for test in stats.homework_tests:
        testik = Test.Test(headers, test)
        testik.continue_test()

        testik.solve_tasks()
        saver = Saver.Saver(headers, testik.continue_id)
        saver.send_answers(testik)


if __name__ == "__main__":
    while True:
        test_stats()
        sleep(1)
