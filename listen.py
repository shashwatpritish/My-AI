import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
    except:
        return ""
    query = str(query).lower()
    return query


# और क्या हुआ सब ठीक है
# print(Listen())