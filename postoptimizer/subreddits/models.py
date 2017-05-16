from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SubredditStats(models.Model):

    
    subreddit_name = models.CharField(_('Name of Subreddit'), blank=False, max_length=255)

    timestamp = models.DateField(_('Time of Stats'), blank=False)

    time_bucket = models.CharField(_('Stringified List of Best Times'), blank=False, max_length=127)
    weekday_bucket = models.CharField(_('Stringified List of Best Weekdays'), blank=False, max_length=127)

    def __str__(self):
        return "Stats for " + self.subreddit_name + " from " + str(self.timestamp)