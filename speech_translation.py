import speech_recognition as sr
import pyttsx3
from googletrans import translator
def speak(text,language="en")
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    voices = engine.getproperty('voices')
    if language =="en":
        engine.setProperty('voice',voices[0].id)
    else
        engine.setProperty('voice',voices[1].id)
        
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognize = sr.Recognizer()
    with sr.Microphone as source:
        print("????Please speak now in English....")
        audio = recognizer.listen(source)
    try
        print("????Recognizing speach....")
        text = recognizer.recognize_google(audio,language "english US")
        print(f"you said{text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"API ERROR:{e}")
        return ""
def translate_text(text, target_language="es"):
    translator=Translator()
    translation=translator.translate(text,dest target_language)
    print("????Translated text {translatio.text}")
    return translation.text
def dispaly_language_options():
    print("????Available translation languages:")
    print("1.Hindi(hi)")
    print("2.Tamil(ta)")
    print("3.Telugu(te)")
    print("4.Bengali(bn)")
    print("5.Marathi(mr)")
    print("6.Hindi(hi)")