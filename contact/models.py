from django.db import models

class ContactRequest(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)
    content = models.TextField(max_length=1200)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.email}, {self.name}'