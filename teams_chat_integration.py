import requests
import json
import os
# from logger_file import logger

# Microsoft Graph API Credentials
CLIENT_ID = "03a9f980-1f6f-479a-8af5-53dc8008270f"
CLIENT_SECRET = "onp8Q~fdd5hdy8yUVxzBZgoUyyPwBu1VxFlRjdyS"
TENANT_ID = "e0d55dd0-7e8b-45fb-9c81-c4ad071c91dd"
GRAPH_API_URL = "https://graph.microsoft.com/v1.0"

# TENANT_ID = "e0d55dd0-7e8b-45fb-9c81-c4ad071c91dd"
# CLIENT_SECRET = "Tke8Q~oNzin~ok4IKMQnHMe6ilESNWSxDeLChctI"
# CLIENT_ID = "0244af74-405d-4c6d-9334-3f1b00b69b53"


def get_access_token():
    """
    Get OAuth2 access token from Microsoft Graph API.
    """
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get token: {response.text}")


def get_user_id(access_token, user_email):
    """
    Get the Microsoft Entra ID (AAD) user ID using the email address.
    """
    url = f"{GRAPH_API_URL}/users/{user_email}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["id"]  # Return the user ID
    else:
        raise Exception(f"Failed to get user ID: {response.text}")


def get_chat_id(access_token, user_id):
    """
    Retrieve the chat ID for a specific user using Application Permissions.
    """
    url = f"{GRAPH_API_URL}/users/{user_id}/chats"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        chats = response.json().get("value", [])
        if chats:
            return chats[0]["id"]  # Get the first chat ID
        else:
            raise Exception("No chat found for this user.")
    else:
        raise Exception(f"Failed to get chat ID: {response.text}")


def upload_file_to_chat(access_token, chat_id, file_path):
    """
    Upload a file to a Microsoft Teams chat.
    """
    url = f"{GRAPH_API_URL}/chats/{chat_id}/filesFolder/children"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    file_name = os.path.basename(file_path)
    file_metadata = {
        "@microsoft.graph.conflictBehavior": "rename",
        "name": file_name
    }

    response = requests.post(url, headers=headers, json=file_metadata)

    if response.status_code == 201:
        upload_url = response.json()["@microsoft.graph.uploadUrl"]

        with open(file_path, "rb") as file:
            upload_response = requests.put(upload_url, data=file)

        if upload_response.status_code in [200, 201]:
            return f"File uploaded successfully: {file_name}"
        else:
            raise Exception(f"File upload failed: {upload_response.text}")
    else:
        raise Exception(f"Failed to create upload session: {response.text}")


def send_message_with_file(access_token, chat_id, message, file_name):
    """
    Send a message to a Teams chat with a file attachment reference.
    """
    url = f"{GRAPH_API_URL}/chats/{chat_id}/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    message_data = {
        "body": {
            "content": f"{message}\n\n📎 File: {file_name}"
        }
    }

    response = requests.post(url, headers=headers, json=message_data)

    if response.status_code == 201:
        return "Message sent successfully!"
    else:
        raise Exception(f"Failed to send message: {response.text}")


if __name__ == "__main__":
    # Replace with actual values
    user_email = "smartestuser1@relanto.ai"
    file_path = r"C:\Users\Supreeth\Downloads\proxy.config.json"
    message = "Here is the file you requested!"

    try:
        # Get access token
        access_token = get_access_token()
        print(f"Access Token: {access_token}")

        # Get user ID
        user_id = get_user_id(access_token, user_email)
        print(f"User ID: {user_id}")

        # Get chat ID
        chat_id = get_chat_id(access_token, user_id)
        print(f"Chat ID: {chat_id}")

        # Upload file
        # upload_status = upload_file_to_chat(access_token, chat_id, file_path)
        # print(upload_status)

        # Send message
        message_status = send_message_with_file(access_token, chat_id, message, os.path.basename(file_path))
        print(f"Message Status: {message_status}")
        print(f"Message sent successfully to Teams channel {chat_id}.")

    except Exception as e:
        print(f"Error: {e}")
