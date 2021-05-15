from unittest import TestCase


class LoadUiTest(TestCase):
    def test_load_ui(self):
        testval = True
        with open('../../main.ui', 'r') as f:
            data = f.read()
        self.assertTrue(data, testval)
