import os

import requests

channel = "#general"
messages = dict(
    A1="재택 근무자는 출근하시면 스레드 댓글로 간단하게 남겨주세요. ex) 출근",
    A2="출근시 Daily Goal을 간단하게 남겨주세요.",
    A3="퇴근하시면 스레드 댓글로 간단하게 남겨주세요. ex) 퇴근",
    A4="퇴근시 Daily Goal 달성율을 간단하게 남겨주세요."
)


def post_message(token, channel, text):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + token},
                  data={"channel": channel, "text": text}
                  )


def lambda_handler(event, context):
    bot_type = event.get("bot_type")
    message = messages.get(bot_type)
    slack_token = os.environ.get("SLACK_TOKEN")

    post_message(slack_token, channel, message)
