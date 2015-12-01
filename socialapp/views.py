from django.shortcuts import render, redirect

from socialapp.models import UserPost, UserPostComment
from socialapp.forms import UserPostForm, UserPostCommentForm


def index(request):
    posts = UserPost.objects.order_by('-date_added')
    context = {
        'posts': posts
    }
    if request.method == 'GET':
        form = UserPostForm()
        context['form'] = form
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            user_post = UserPost(text=text, author=author)
            user_post.save()
            return redirect('index')
        else:
            context['form'] = form
            return render(request, 'index.html', context)


def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    title = post.text[:15] + "[...]"
    comments = UserPostComment.objects. \
            filter(post=post).order_by('-date_added')
    context = {
        'post': post, 
        'title': title,
        'comments': comments,
    }
    if request.method == 'GET':
        form = UserPostCommentForm()
        context['form'] = form
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            user_comment = UserPostComment(text=text, author=author, post=post)
            user_comment.save()
            return redirect('post_details', pk=pk)
        else:
            context['form'] = form
            return render(request, 'post_details.html', context)







