import speech_recognition as sr
import datetime
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('CLEARING AMBIENT NOISES\nEqualizing volume\nPlease wait...\n\n')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything: ')
        recordedaudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recordedaudio)
        print("You said: ", command)

        #Handle the recognized command
        if 'play' in command:
            song= command.replace('play','')
            print('playing',song)
            pywhatkit.playonyt(song)
        elif'search ' in command:
            query= command.replace('search','')
            print('searching for',query)
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
        elif'time' in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current time:", current_time)
            engine.say("The current time is " + current_time)  
            engine.runAndWait()
        elif'date' in command:
            today = datetime.date.today()
            print("today's date:",today)
            engine.say("Today's date is " + str(today))
            engine.runAndWait()
        else :
            print("Sorry,I didn't catch that.")




        print("Sorry,I didn't catch that.")
    except sr.RequestError as e:
        print("could not request results;{0}".format(e))

cmd()