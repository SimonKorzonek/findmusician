from django.test import TestCase
from posts.models import Post, Comment
from django.contrib.auth.models import User

class ModelsTest(TestCase):
    def setUp(self):
        User.objects.create(username='user')
        self.user = User.objects.get(username='user')

        self.post = Post.objects.create(
            title='This is a post title',
            author=self.user)
    
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="this is comment")

    def test_post_has_slug(self):
        self.assertEqual(self.post.slug, 'this-is-a-post-title')

    def test_post_str(self):
        self.assertEqual(str(self.post), "This is a post title, user")

    def test_comment_str(self):
        self.assertEqual(str(self.comment), "user, this is comment")
