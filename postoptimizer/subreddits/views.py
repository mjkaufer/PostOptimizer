import urllib2
import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect

from utils import parse_subreddit_data
from .models import SubredditStats



default_header={'User-agent': 'optobot 0.1'}

def update_random(request):
    request_url = "https://www.reddit.com/r/random.json"
    request = urllib2.Request(request_url, headers=default_header)
    json_data = urllib2.urlopen(request).read()
    # print("\n\n\nThis is a test\n\n\n" + serialized_data + "\n\n\n")
    try:
        # print("we in here")
        # parsed_data = json.loads(serialized_data)
        # print("serialize mmmmm\n\n")
        # print(parsed_data)
        # print("1\n\n\n1")
        # print(parsed_data.keys())
        # print("1.5\n\n1.5")
        # print(parsed_data["data"])
        # print("2\n\n2")
        # print(parsed_data["data"]["children"][0])
        # print("3\n\n3")

        subreddit_name = json_data["data"]["children"][0]["data"]["subreddit"]
        # print("got to " + str(subreddit_name))
        return redirect('/subreddits/' + str(subreddit_name))
    except:
        #request didn't go thru - internet is bad or smthn
        return HttpResponse("Uh oh, no internet!", status=500)

    #we'll return the info of a random subreddit subreddits
    # return HttpResponse("Hello, world. You're at the reddit index.")


def update_specific_subreddit(request, subreddit, from_stats=False):
    print("They wanna go to " + subreddit)
    request_url = "https://www.reddit.com/r/" + subreddit + "/top.json?t=month&limit=100"
    request = urllib2.Request(request_url, headers=default_header)
    serialized_data = urllib2.urlopen(request).read()
    json_data = json.loads(serialized_data)

    parsed_data = parse_subreddit_data(json_data["data"]["children"])

    subreddit_stats = SubredditStats(subreddit_name=subreddit,
        timestamp=datetime.now(),
        time_bucket=json.dumps(parsed_data["time_bucket"]),
        weekday_bucket=json.dumps(parsed_data["weekday_bucket"]))

    subreddit_stats.save()


    if from_stats:
        return redirect('/subreddits/stats/' + str(subreddit_name))
    else:
        return HttpResponse(json.dumps(parsed_data), content_type="application/json")

def stats_specific_subreddit(request, subreddit):

    subreddit_query = SubredditStats.objects.filter(subreddit_name=subreddit)
    json_return = {}

    if len(subreddit_query) == 0:
        # if there's no stats for this subreddit yet
        # then we'll call our function to update a specific subreddit
        return redirect('/subreddits/update/' + str(subreddit), from_stats=True)

    cum_keys = ["time_bucket", "weekday_bucket"]



    for subreddit_stat in subreddit_query:
        print("\n\n",str(getattr(subreddit_stat, "time_bucket")),"\n\n")
        for key in cum_keys:
            if key not in json_return:
                json_return[key] = json.loads(getattr(subreddit_stat, key))
            else:
                json_return[key] = map(sum, zip(json_return[key],
                    json.loads(getattr(subreddit_stat, key))))

    json_return["subreddit"] = subreddit

    return HttpResponse(json.dumps(json_return), content_type="application/json")



