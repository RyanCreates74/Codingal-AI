import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import os
import pyjokes

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Please speak now...")
        audio = recognizer.listen(source)

        try:
            print("🔎 Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print(f"❌ API error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

        return ""


def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "google" in command:
        webbrowser.open("google.com")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        quit()


def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        respond_to_command(command)

if __name__ == "__main__":
    main()