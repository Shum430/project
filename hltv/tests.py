from django.test import TestCase
from .models import *


class PlayerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Player.objects.create(name='Oleksandr')


    def test_1(self):
        player = Player.objects.get(id__exact=1)
        p1=str(player)
        p2=player.first
        self.assertEqual(p1,p2)












