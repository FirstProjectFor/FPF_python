import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("初始化资源。。。")

    @classmethod
    def tearDownClass(cls):
        print("释放资源。。。")

    def setUp(self):
        print("set up")

    def tearDown(self):
        print("tearDown")

    @unittest.expectedFailure
    def test_error(self):
        self.assertTrue(1 + 1 != 2, "1+1 != 2")

    def test_method_first(self):
        self.assertTrue(1 + 1 == 2, "1+1 = 2")

    def test_method_second(self):
        self.assertTrue(1 + 2 == 3, "1+2 = 3")

    def test_even(self):
        for i in range(0, 4):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    @unittest.skip("测试跳过")
    def test_skip(self):
        self.assertTrue(True, True)

    def test_skip_in_code(self):
        self.skipTest("测试代码内跳过测试")
