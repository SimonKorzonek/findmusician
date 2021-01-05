from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class UserInstrument(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.name}'

class UserGenere(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.name}'

class UserCooperation(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.name}'

class UserKindOfProfile(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    kind = models.ForeignKey(UserKindOfProfile, on_delete=models.SET_NULL, null=True)
    instruments = models.ManyToManyField(UserInstrument)
    generes = models.ManyToManyField(UserGenere)
    city = models.CharField(max_length=30)
    open_for_coop = models.BooleanField(default=True)
    form_of_coop = models.ManyToManyField(UserCooperation)
    bio = models.CharField(max_length=600)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'slug': self.slug})

    def get_instruments(self):
        return ", ".join(str(instrument) for instrument in self.instruments.all())

    def get_generes(self):
        return ", ".join(str(genere) for genere in self.generes.all())

    def get_form_of_coop(self):
        return ", ".join(str(coop) for coop in self.form_of_coop.all())

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
       ordering = ['-user']