from django.forms import Form, CharField, ChoiceField, DateField, \
        Textarea, PasswordInput, SelectDateWidget, ImageField


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5, 'placeholder': "What's on your mind?"}),
        label='')


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write a comment...'}),
        label='')


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class EditProfileForm(Form):
    first_name = CharField(max_length=100, required=False)
    last_name = CharField(max_length=100, required=False)
    birthday = DateField(widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ), required=False)
    sex = ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), required=False)
    avatar = ImageField(required=False)


