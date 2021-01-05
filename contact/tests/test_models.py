from django.test import TestCase
from contact.models import ContactRequest

class ModelsTest(TestCase):
    def setUp(self):
        ContactRequest.objects.create(
            email='email@email.com',
            name='name')
        self.contact_request = ContactRequest.objects.get(email='email@email.com')

    def test_contact_request_str(self):
        self.assertEqual(str(self.contact_request), "email@email.com, name")
