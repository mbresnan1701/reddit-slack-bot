import os
import slack
import re
from reddithandler import get_from_reddit

api_token = os.environ['SLACK_BOT_TOKEN']

client = slack.WebClient(token=api_token)
rtm_client = slack.RTMClient(token=api_token)

whitelisted_subreddits = { 'prequelmemes', 'aww' }

help_message = 'Hi User. Currently available subreddits are: ' + str(whitelisted_subreddits)

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    channel_id = data['channel']
    text = data.get('text')

    if text is not None:
        trigger_text = re.search('^rb\s(\w+)', text)
        if trigger_text is not None:
            submitted_command = trigger_text.group(1)
            print(whitelisted_subreddits)
            if submitted_command in whitelisted_subreddits:
                link = get_from_reddit(submitted_command)

                if link is not None:
                    web_client.chat_postMessage(channel=channel_id, text=link)

            elif submitted_command == "help":
                web_client.chat_postMessage(channel=channel_id, text=help_message)


rtm_client.start()
