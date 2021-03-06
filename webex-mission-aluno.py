import ??? # MISSION: Module name is missing
import json

# Global variables

access_token = "???" # MISSION: Token can be obtained from https://developer.webex.com/docs/api/getting-started

httpHeaders = {"Content-type": "application/json",
           "Authorization": "Bearer " + access_token}

room_id = "???" # MISSION: room_id obtained from Webex API documentation

def post_message(room_id):

    """
    This function will post a message to the
    room based on provided room ID
    """
    text = input("What message would you like to post? ")
    apiUrl = "???" # MISSION: Provide the resource URL for creating Messages
    body = {"roomId": room_id, "text": text}

    response = requests.???(url=apiUrl, json=body, headers=httpHeaders) #MISSION: requests method is missing

    if response.status_code == 200:
        print("Your message was successfully posted to the room")
    else:
        print("Something went wrong.\n"
              "Please check the script and run it again!")
        exit()

def main():

    """
    Main function
    """
    post_message(room_id)


if __name__ == "__main__":
    main()