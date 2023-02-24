# Importing the files
# *******************
from listen import Listen
from speak import Speak
from brain import reply
from clap import Tester
from time import sleep
from random import randint

# Coding
# ******

Tester()
sleep(randint(1,5))
Speak("Welcome sir, I am jarvis created by Shashwat-the hacker. You can ask any question")

def MainExecution():
    while True:
        query = Listen()
        kk = reply(query)
        print(Speak(kk))
    
MainExecution()