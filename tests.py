from mongoengine import *
import unittest
from models import *

class Test(unittest.TestCase):
    @classmethod
    def setUp(cls):
        connect('mongoenginetest', host='mogomock://localhost')

    @classmethod
    def tearDown(cls):
        disconnect()

    def