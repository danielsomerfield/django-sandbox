from django.test import TestCase

from catservice.domain.cat import Cat


class CatServiceTestCase(TestCase):
    def setUp(self):
        self.cat = Cat("Rufus")

    def test_pet(self):
        self.assertEqual(self.cat.pet(), "purr")
