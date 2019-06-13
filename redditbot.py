import os
import slack
from reddithandler import get_from_reddit

api_token = os.environ['SLACK_BOT_TOKEN']

client = slack.WebClient(token=api_token)
rtm_client = slack.RTMClient(token=api_token)

subreddit_map = {
    'hello there': 'prequelmemes',
    'show me a funny': 'funny'
}

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    channel_id = data['channel']
    text = data.get('text')

    if text is not None:
        link = None

        for activator in subreddit_map.keys():
            if activator in text:
                link = get_from_reddit(subreddit_map[activator])
                break

        if link is not None:
            web_client.chat_postMessage(channel=channel_id, text=link)


rtm_client.start()
