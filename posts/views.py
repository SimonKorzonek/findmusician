from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form = PostForm
    fields = ['title', 'text']
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post-list')
    success_message = "Your post has been added."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form = PostForm
    template_name = 'posts/post_form.html'
    fields = ['title', 'text']
    success_message = "Your post has been updated."


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'posts/post_delete.html'
    success_message = 'Your post has been deleted.'

    # no form.is_valid() in DeleteView to push msg to user
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.all()
        #replies = CommentReply.objects.all()
        context['comments'] = comments
        #context['replies'] = replies
        return context


class PostDetailView(SuccessMessageMixin, DetailView):
    model = Post
    success_message = 'Your comment has been added.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_comments = Comment.objects.all().order_by('-created')
        context['comments'] = post_comments

        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            text = request.POST.get('text'),
            author = self.request.user.profile,
            parent = None,
            post = self.get_object())

        new_comment.save()
        messages.success(self.request, self.success_message)
        return self.get(self, request, *args, **kwargs)


class CommentDetailView(SuccessMessageMixin, DetailView):
    model = Comment
    success_message = 'Your reply has been added.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_replies = Comment.objects.filter(comment=self.get_object()).order_by('-created')
        post = Post.objects.get(comments=self.get_object())
        context['post'] = post
        context['replies'] = comment_replies
        if self.request.user.is_authenticated:
            context['comment_reply_form'] = CommentForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None

        if parent_id:
            parent_queryset = Comment.objects.filter(id=parent_id)
            if parent_queryset.exists() and parent_queryset.count() == 1:
                parent = parent_queryset.first()

        new_reply = Comment(
            parent_id = self.get_object().id,
            text = request.POST.get('text'),
            author = self.request.user.profile,
            parent = request.POST.get('parent_id'))

        new_reply.save()
        messages.success(self.request, self.success_message)
        return self.get(self, request, *args, **kwargs)