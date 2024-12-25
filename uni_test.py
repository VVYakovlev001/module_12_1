import HumanMoveTest
import unittest


class RunnerTest(unittest.TestCase):


    def test_walk(self): # метод, в котором создаётся объект класса Runner с произвольным именем.
        runner = HumanMoveTest.Runner('Вася')
        for _ in range(10): # вызовите метод walk у этого объекта 10 раз
            runner.walk()
        self.assertEqual(runner.distance, 50) #  методом assertEqual сравните distance этого объекта со значением 50.


    def test_run(self): # метод, в котором создаётся объект класса Runner с произвольным именем.
        runner = HumanMoveTest.Runner('Петя')
        for _ in range(10): # вызовите метод run у этого объекта 10 раз.
            runner.run()
        self.assertEqual(runner.distance, 100) # сравните distance этого объекта со значением 100.


    def test_challenge(self): # метод в котором создаются 2 объекта класса Runner с произвольными именами
        runner1 = HumanMoveTest.Runner('Вася')
        runner2 = HumanMoveTest.Runner('Петя')
        for _ in range(10): # Далее 10 раз у объектов вызываются методы run и walk соответственно.
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance) #  используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.




if __name__ == '__main__':
    unittest.main()
