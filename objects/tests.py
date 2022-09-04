from django.test import TestCase
from django.utils import timezone
import string
import random
from .models import *

class TestRecords(TestCase):

    def setup():
        get_randowm_string = lambda lenght, start="",charts=string.ascii_uppercase : (start.join(random.choice(charts)) for _ in range(lenght))
        a = Area(name = get_randowm_string(lenght = 5), atention=5)
        pass
    
    def test_area():
        pass
    
    def test_device():
        pass
    
    def test_worker():
        pass
    