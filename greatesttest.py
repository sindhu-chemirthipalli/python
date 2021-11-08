import unittest
from service.great import great
class largest(unittest.TestCase):
    def testgreat1(self):
        self.assertEqual(great(2,3,5),5)

    def testgreat2(self):
        self.assertEqual(great(2.5,0,5 ),5)

    def testgreat3(self):
        self.assertEqual(great(-1,2,6 ),6)

    def testgreat4(self):
        self.assertEqual(great(-0.5,-1,-3 ),-0.5)

    def testgreat5(self):
        self.assertEqual(great("a",5,3),"error")

    def setUp(self) :
        print("setup")





