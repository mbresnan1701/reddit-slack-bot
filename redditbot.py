import os
import time
import re
import slack

api_token = os.environ['SLACK_BOT_TOKEN']

client = slack.WebClient(token=api_token)
rtm_client = slack.RTMClient(token=api_token)


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'hello there' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f'General Kenobi!',
            # thread_ts=thread_ts
        )


rtm_client.start()

