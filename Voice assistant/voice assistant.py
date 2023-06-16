import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    # Function to speak the provided text
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # Function to wish the user based on the current time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Chloe. Please tell me how may I help you")


def takeCommand():
    # Function to take microphone input from the user and return the recognized text
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            # Search and speak information from Wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # Open YouTube in a web browser
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            # Open Google in a web browser
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            # Open facebook in a web browser
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            # Play music from a specified directory
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            # Play videos from a specified directory
            music_dir = 'E:\\Video'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            # Get the current time and speak it
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open folder' in query:
            # Open Visual Studio Code folder
            codePath = "C:\\Users\\Ayesha\'s PC\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif "exit" in query:
            # End the program
            speak("Ending program. Thanks for using Chloe")
            print("Thank you for using CHLOE <3")
            break
