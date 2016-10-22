from django.conf.urls import url
from scribble import views

app_name = "scribble"
urlpatterns = [
    url(r'^artwork/(?P<pk>[0-9]+)$', views.ArtworkDetail.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^comment/$', views.CommentCreate.as_view()),
    url(r'^like/$', views.LikeCreate.as_view()),
    url(r'^newuser/$', views.UserCreate.as_view()),
    url(r'^artwork/$', views.ArtworkCreate.as_view()),
    url(r'^discover/$', views.Discover.as_view()),
]