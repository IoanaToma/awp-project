from django.forms import Form, CharField, Textarea, TextInput


class UserPostForm(Form):
    author = CharField(widget=TextInput(),
        label="Enter your name here")
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your post here")


class UserPostCommentForm(Form):
    author = CharField(widget=TextInput(), 
        label="Enter your name here")
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your comment here")
