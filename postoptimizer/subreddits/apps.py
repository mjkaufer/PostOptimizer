from __future__ import unicode_literals

from django.apps import AppConfig


class SubredditsConfig(AppConfig):
    name = 'postoptimizer.subreddits'
    verbose_name = 'subreddit stats stuff'

    def ready(self):
        
        # from .models import SubredditStats
        
        pass
