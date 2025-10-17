import os
import time
from datetime import datetime
import requests
import functions_framework


def send_google_chat_message(message, google_chat_webhook):
    """Send a message to Google Chat."""
    headers = {"Content-Type": "application/json"}
    data = {"text": message}

    GOOGLE_CHAT_WEBHOOK = google_chat_webhook
    
    response = requests.post(GOOGLE_CHAT_WEBHOOK, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.status_code}, {response.text}")

@functions_framework.http
def send_noti(request):
    
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y_%H:%M:%S")

    # Webhook List
    de_webhook = "https://chat.googleapis.com/v1/spaces/AAQA4vVH8yY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=mDogCDO_DXBkboDcHu6YLs8nds4F589Y7-Gh6mwsNNI"
    webhook_list = [de_webhook]

    # Noti Message
    noti = f"Test Noti Time: {formatted_now}."

    for wbhook in webhook_list:
        message = noti
        google_chat_webhook = wbhook
        send_google_chat_message(message, google_chat_webhook)    
    print("Notification Sent.")
    return "Notification sent."


    