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

    def test_error(self):
        self.assertTrue(1 + 1 != 2, "1+1 != 2")

    def test_method_first(self):
        self.assertTrue(1 + 1 == 2, "1+1 = 2")

    def test_method_second(self):
        self.assertTrue(1 + 2 == 3, "1+2 = 3")

    @unittest.skip("测试跳过")
    def test_skip(self):
        self.assertTrue(True, True)
