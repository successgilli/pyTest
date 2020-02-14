from app import app

import unittest

class TestApp(unittest.TestCase):

    def test_land(self):
        apptest = app.test_client(self)
        res = apptest.get('/')
        self.assertEqual(res.data, b'welcome home')

if __name__ == '__main__': unittest.main()
