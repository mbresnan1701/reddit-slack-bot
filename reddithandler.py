import requests
import re
import random


def get_from_reddit(subreddit):
    link = 'https://www.reddit.com/r/' + subreddit + '/hot/.json?limit=50'
    res = requests.get(link, headers={'User-agent': 'the senate 0.1'})

    if res.status_code == 200:
        picked_link = filter_usable_links(res.json())

        if(picked_link):
            return picked_link
        else:
            return "PICK FAILURE"
    else:
        return "API FAILURE"


def filter_usable_links(response_json):
    posts = list(filter(image_filter, response_json['data']['children']))

    if len(posts) == 0:
        return "FILTER FAILURE"

    random_post = random.choice(posts)

    url = random_post.get('data').get('preview').get('images')[0].get('source').get('url')

    if url is not None:
        return replace_preview(url)
    else:
        return None


def image_filter(post):
    if post.get('data') and post.get('data').get('preview'):
        source_url = post.get('data').get('preview').get('images')[0].get('source').get('url')
        if '//preview.redd.it' in source_url:
            return True
        else:
            return False
    return False


def replace_preview(url):
    regex_search = "preview.redd.it"
    regex_replace = "i.redd.it"

    return re.sub(regex_search, regex_replace, url)
