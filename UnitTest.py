from Menu import Menu
import unittest
class Test(unittest.TestCase):
    __menu: Menu

    def setUp(self) -> None:
        self.__menu = Menu()
    def test_menu(self):
        self.__menu = Menu()
        self.__menu.menu()

if __name__ == '__main__':
    unittest.main()