import os
from dotenv import load_dotenv
import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from stti import SpeechToTextInterpreter
from ttsi import TextToSpeechPrinter
load_dotenv()

token = os.environ.get("COOKIE_1")
cookie_2 = os.environ.get("COOKIE_2")
cookie_3 = os.environ.get("COOKIE_3")
cookie_4 = os.environ.get("COOKIE_4")

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set("__Secure-1PSIDTS", cookie_2)
session.cookies.set("__Secure-1PSIDCC", cookie_3)
session.cookies.set("GOOGLE_ABUSE_EXEMPTION", cookie_4)

bard = Bard(token=token, session=session)


class Chatbot():
    def __init__(self):
        self.name = "luke skywalker"
        self.user_name = "user "

    def save_user_info(self, user_name):
        self.user_name = user_name

    def get_user_info(self):
        print("What is your name?  ")
        name = input("")
        self.save_user_info(name)
        print(f"Welcome {name}")

    def get_response(self, user_input):
        bad_chars =['*', '**', '[', ']', '\\', '/chat.py']
        response = bard.get_answer(user_input)['content']
        for char in bad_chars:
            response = response.replace(char, '')
        return response
    

    def chat(self):
        print(f"Hello I'm {self.name}")
        self.get_user_info()
        # print("What can i do for you Today")
        while True:
            user_input = input("How may I assist you ")
            if user_input.lower() == "quit":
                print("May the force be with you! ")
                break

            response = self.get_response(user_input)
            print(response)
with TextToSpeechPrinter(), SpeechToTextInterpreter():
   chatbot = Chatbot()
   chatbot.chat()

# python -m venv venv

# venv\scripts\activate

# venv\Scripts\activate