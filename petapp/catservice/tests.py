from django.test import TestCase
from django.test import Client
import json
from unittest import skip


class CatServiceTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health(self):
        response = self.client.get('/cats/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_pet_cat(self):
        response = self.client.post("/cats/fluffy/pet")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'cat': 'fluffy', 'action': 'purr'})

    def test_pet_cat_with_brush(self):
        response = self.client.post("/cats/purrington/brush", json.dumps({'brush_type': "ouchy"}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'cat': 'purrington', 'action': 'scratch'})

    # @skip("NYI")
    def test_pet_cat_with_comfy_brush(self):
        response = self.client.post("/cats/purrington/brush", json.dumps({"brush_type": "comfy"}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'cat': 'purrington', 'action': 'purr'})
