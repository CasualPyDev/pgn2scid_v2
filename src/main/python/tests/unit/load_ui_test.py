from unittest import TestCase
from main import Ui


class LoadUiTest(TestCase):
    def test_load_ui(self):
        testval = True
        with open('../../ui/main.ui', 'r') as f:
            data = f.read()
        self.assertTrue(data, testval)
