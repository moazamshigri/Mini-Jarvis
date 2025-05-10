import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def handle_command(command):
    command = command.lower()

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open stack overflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://twitter.com")

    elif "exit" in command:
        speak("Thanks for using me. Shutting down now.")
        exit()  # <-- This kills the program completely


    else:
        speak("I don't recognize that command yet.")
    
    return True  # remain active

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    jarvis_active = False

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            try:
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
                query = recognizer.recognize_google(audio).lower()
                print(f"You said: {query}")

                if not jarvis_active:
                    if "jarvis" in query:
                        speak("Yes, I’m here.")
                        jarvis_active = True
                else:
                    jarvis_active = handle_command(query)

            except sr.WaitTimeoutError:
                print("⏱️ Timeout")
                continue
            except sr.UnknownValueError:
                print("🤷 Didn't understand that.")
                continue
