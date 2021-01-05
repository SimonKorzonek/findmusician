from django.test import TestCase
from contact.models import ContactRequest
from django.test import Client

csrf_client = Client(enforce_csrf_checks=True)

class TestContactRequest(TestCase):
    def test_can_send_message(self):

        data = {
            "email": "blambor@gmail.com",
            "name": "name",
            "content": "content",
            "date": "2021-01-04 17:07:02.582204+00:00",
        }

        response = self.client.get("/contact/")
        self.assertContains(response, "email")
        self.assertContains(response, "name")
        self.assertContains(response, "content")
        response = self.client.post("/contact/", data=data)
        self.assertEqual(ContactRequest.objects.count(), 1)