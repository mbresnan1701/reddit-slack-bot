import requests
import random


def get_from_reddit(subreddit):
    link = 'https://www.reddit.com/r/' + subreddit + '/top/.json?sort=top&t=day&limit=50'
    res = requests.get(link, headers={'User-agent': 'the senate 0.1'})

    if res.status_code == 200:
        picked_link = filter_usable_links(res.json())

        if picked_link:
            return picked_link
        else:
            return "PICK FAILURE"
    else:
        return "API FAILURE"


def filter_usable_links(response_json):
    posts = list(filter(image_filter, response_json['data']['children']))
    print(len(posts))
    if len(posts) == 0:
        return "FILTER FAILURE"

    random_post = random.choice(posts)

    url = random_post.get('data').get('url')

    if url is not None:
        return random_post.get('data').get('title') + ' ' + url
    else:
        return None


def image_filter(post):
    data = post.get('data')
    if data and data.get('url'):
        if 'i.redd' in data.get('url'):
            if data.get('over_18') is not False:
                return False

            return True

    return False
