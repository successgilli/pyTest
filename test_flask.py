from app import app

import unittest

class TestApp(unittest.TestCase):

    def test_land(self):
        apptest = app.test_client(self)
        res = apptest.get('/')
        self.assertEqual(res.status, '200 OK')
    
    def test_body(self):
        tester = app.test_client(self)
        res = tester.get('/')
        print(res)
        self.assertEqual(res.data, b'{"data":"welcome","status":200}\n')

if __name__ == '__main__': unittest.main()
