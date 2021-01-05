from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import django.utils.timezone
from django.contrib.auth.models import User
from users.views import Profile


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=1200)
    created = models.DateField(default=django.utils.timezone.now)
    slug = models.SlugField(blank=True, null=True)

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta: 
        ordering = ('created',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=420)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def children(self):  # replies
        return Comment.objects.filter(parent=self)

    class Meta: 
        ordering = ('created',)

    def __str__(self):
        return f'{self.author}, {self.text}'