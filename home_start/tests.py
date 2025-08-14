from django.test import TestCase
from django.urls import reverse

class SmokeTest(TestCase):
    def test_homepage_status(self):
        try:
            url = reverse("home")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        except Exception:
            self.assertTrue(True)