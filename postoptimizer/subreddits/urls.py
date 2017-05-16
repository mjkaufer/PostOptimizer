from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^update$', views.update_random, name='update_random'),#go to random subreddit if they're not specific
    url(r'^update/(?P<subreddit>[\w.@+-]+)$', views.update_specific_subreddit, name='update_specific_subreddit'),
    # url(r'^stats$', views.stats_random_subreddit, name='stats_random_subreddit'),
    url(r'^stats/(?P<subreddit>[\w.@+-]+)$', views.stats_specific_subreddit, name='stats_specific_subreddit'),
]