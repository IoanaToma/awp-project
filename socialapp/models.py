from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class UserPost(models.Model):
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(
        auto_now_add=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserPostComment(models.Model):
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(UserPost, related_name='comments')

    class Meta:
        ordering = ['date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        )
    first_name = models.TextField(max_length=500)
    last_name = models.TextField(max_length=500)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, 
        choices=(('M', 'Male'), ('F', 'Female')), default='M')
    avatar = models.ImageField(upload_to='avatars/',
        default='avatars/dog_with_puppies.jpg')

    def __unicode__(self):
        return u'{} @ {}'.format(self.first_name, self.last_name)



