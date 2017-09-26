from .. import secrets
from slackclient import SlackClient

slack_token = secrets.slack_api_token
sc = SlackClient(slack_token)

def publish(quote):
    sc.api_call(
      "chat.postMessage",
      channel="#quotes",
      text= "{}".format(quote)
    )
