from datetime import datetime

def parse_subreddit_data(data):
    # analyzes
    bucket = make_empty_bucket()

    for post in data:
    
        timestamp = post["data"]["created"]
        
        datetime_object = datetime.fromtimestamp(timestamp)
            
        bucket[datetime_object.weekday()][datetime_object.hour / 2] += 1
        # bucket[datetime_object.weekday()]["total"] += 1
        bucket["total"] += 1
    bucket["weekday_bucket"] = [sum(bucket[k]) for k in bucket if type(bucket[k]) is list]
    best_time = bucket[0]
    for i in range(1, 7):
        best_time = map(sum, zip(best_time, bucket[i]))
    bucket["time_bucket"] = best_time#in resolution of BUCKET_RESOLUTION hours
    # bucket["updated_at"] = datetime.now()

    ##TODO, have some way to check if we're looking at inactive subreddit
    ##or like check the change in time since last check or smthn

    # print(x)
    # best_days = list(map(lambda y: sum(y), x))
    # print(best_days)
    # print("^best")


    return bucket;


BUCKET_RESOLUTION = 2 #hours

def make_empty_bucket():
    bucket = {}
    for i in range(0, 7):
        bucket[i] = [0] * (24 / BUCKET_RESOLUTION)
        

    bucket["total"] = 0

    return bucket
