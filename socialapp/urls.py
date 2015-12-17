from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from socialapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^user_profile/(?P<username>[A-Za-z]+)/$', views.user_profile, name='user_profile'),
    url(r'^edit_profile/(?P<username>[A-Za-z]+)/$', views.edit_profile, name='edit_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
