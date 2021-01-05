from django.test import TestCase
from users.models import Profile, UserKindOfProfile, UserGenere, UserInstrument, UserCooperation
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="the username 1 12")
        UserKindOfProfile.objects.create(name='kind no.1')
        UserInstrument.objects.create(name='guitar')
        UserGenere.objects.create(name='jazz')

        self.profile = Profile.objects.get(user=self.user)
        self.profile.kind = UserKindOfProfile.objects.get(name='kind no.1')
        self.profile.instrument = UserInstrument.objects.get(name='guitar')
        self.profile.genere = UserGenere.objects.get(name='jazz')


    def test_profile_has_slug(self):
        self.assertEqual(self.profile.slug, 'the-username-1-12')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "the username 1 12")

    def test_kind_str(self):
        self.assertEqual(str(self.profile.kind.name), "kind no.1")

    def test_instrument_str(self):
        self.assertEqual(str(self.profile.instrument.name), "guitar")

    def test_genere_str(self):
        self.assertEqual(str(self.profile.genere.name), "jazz")


