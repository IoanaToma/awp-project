from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from socialapp.forms import UserPostForm, UserPostCommentForm, UserLoginForm, EditProfileForm
from socialapp.models import UserPost, UserPostComment, UserProfile


@login_required
def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text, author=request.user)
            user_post.save()
        return redirect('index')


@login_required
def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserPostCommentForm()
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = UserPostComment(text=text, post=post, author=request.user)
            comment.save()
        return redirect('post_details', pk=pk)


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_profile(request, username):
    if request.method == 'GET':
        user = User.objects.filter(username=username)
        profile = UserProfile.objects.filter(user=user).first()
        context = {'profile': profile}
        return render(request, 'user_profile.html', context)


@login_required
def edit_profile(request, username):
    if request.method == 'GET':
        form = EditProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'edit_profile.html', context)
    elif request.method == 'POST':
        form = EditProfileForm(request.POST)
        user = User.objects.filter(username=username)
        profile = UserProfile.objects.get(user=user)

        print "Image is : {0}".format(form['avatar'].value())

        # if form['first_name'].value():
        #     profile.first_name = form.cleaned_data['first_name']
        # if form['last_name'].value():
        #     profile.last_name = form.cleaned_data['last_name']
        # if form['birthday'].value():
        #     profile.birthday = form.cleaned_data['birthday']
        # if form['sex'].value():
        #     profile.gender = form['sex'].value()
        if form['avatar'].value() is not None:
            profile.avatar = form['avatar'].value()

        profile.save()

        return redirect('user_profile', username=username)
