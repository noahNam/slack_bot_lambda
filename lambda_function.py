from lib import requests


def post_message(token, channel, text):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + token},
                  data={"channel": channel, "text": text}
                  )


def lambda_handler():
    full_msg = "test 입니다"
    slack_token = "xoxb-1234"
    post_message(slack_token, "#bot-test", full_msg)


if __name__ == '__main__':
    lambda_handler()
