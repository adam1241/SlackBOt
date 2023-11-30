import openai
import requests
from bs4 import BeautifulSoup

API_key = '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'

def get_website_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"Erreur lors de la récupération du site web : {e}")
        return None
    
website_url1 = 'https://planktoscope.github.io/PlanktoScope/'
website_url2 = 'https://planktoscope.github.io/PlanktoScope/hardware/manufacturing/'
website_url3 = 'https://planktoscope.github.io/PlanktoScope/hardware/assembly_guide/'
website_url4 = 'https://planktoscope.github.io/PlanktoScope/hardware/maintenance_repair/'
website_url5 = 'https://planktoscope.github.io/PlanktoScope/software/easy_install/'
website_url6 = 'https://planktoscope.github.io/PlanktoScope/software/expert_setup/'
website_url7 = 'https://planktoscope.github.io/PlanktoScope/software/create_sd/'
website_url8 = 'https://planktoscope.github.io/PlanktoScope/usage/getting_started/'
website_url9 = 'https://planktoscope.github.io/PlanktoScope/usage/ui_guide/'


website_text = get_website_text(website_url1) , get_website_text(website_url2) , get_website_text(website_url3) , get_website_text(website_url4),  get_website_text(website_url5 ) , get_website_text(website_url6) , get_website_text(website_url7) , get_website_text(website_url8) , get_website_text(website_url9)
    



import os

from slack_sdk import WebClient

from slack_sdk.errors import SlackApiError


# Initialize a Web API client


client = WebClient(token="xoxb-6102082131061-6112088037186-T2UHPKLINTiHBmiVaJJDy8Pf")


# Listen to messages in a channel
def listen_to_channel():
    # Get the last message in the channel

  result = client.conversations_history(channel="C0637BSF5A7", limit=1)
  last_message = result["messages"][0]["text"]
  user = result["messages"][0]["user"]
  return last_message, user, result
    
# Listen to messages in a group


# Send a message to a channel
def send_message(channel_id, message):
    try:
        result = client.chat_postMessage(channel=channel_id, text=message)
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")


# Main function
if __name__ == "__main__":
    channel_id = "C0637BSF5A7"

    while True:
        last_message, user, result = listen_to_channel()

        if user != 'U063A2L135G':
            if result['messages'][0]['blocks'][0]['elements'][0]['elements'][0]['user_id'] == 'U063A2L135G' :
                send_message(channel_id, f"Hi <@{user}>! Let me think... ")
            # if "hello" in last_message.lower():
            #     send_message(channel_id, f"Hi <@{user}>! Hello! How can I assist you." )
            # elif "how are you" in last_message.lower():
            #     send_message(channel_id, f"Hi <@{user}>! I'm just a bot, but I'm here to help!" )

            #Poser la question dans le content de "user"
                messages = [{"role": "system", "content": "You are a helpful assistant, you will use your information and those informations : {website_text} in order ton answer user's questions."},
                        {"role" : "user", "content" : last_message}]
                response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=messages,
                            api_key = API_key)
                
                send_message(channel_id, f" {response.choices[0].message.content} ")

                print(response.choices[0].message)  