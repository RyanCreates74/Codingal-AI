import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

# Initialize TTS engine once
engine = pyttsx3.init('sapi5')

def setup_voice(language="en"):
    voices = engine.getProperty('voices')

    for i, v in enumerate(voices):
        print(i, v.name)

    # Try to select a suitable voice
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 150)


def speak(text, language="en"):
    setup_voice(language)
    print(f"🔊 Speaking: {text}")
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Please speak now...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("🔎 Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

    return ""


def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(f"🌍 Translated text: {translated}")
        return translated
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return ""


def display_language_options():
    print("\n🌐 Select target language:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. French (fr)")

    choice = input("Enter choice (1-9): ")

    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa",
        "9": "fr"
    }

    return language_dict.get(choice, "en")


def main():
    target_language = display_language_options()

    original_text = speech_to_text()

    if not original_text:
        print("⚠️ No speech detected.")
        return

    translated_text = translate_text(original_text, target_language)

    if translated_text:
        speak(translated_text, language=target_language)
        print("✅ Done!")


if __name__ == "__main__":
    main()