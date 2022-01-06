# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

#Set your name
name = 'Kemor'

# Define a recognizer
r = sr.Recognizer()

# Define an engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)

# Define a function which let us hear what bot says
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Define a function that takes input from our microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = r.listen(source)
            query = r.recognize_google(voice)
            query = query.lower()
            print(query)
    except:
        pass
    return query

# Define a function which makes our bot greet us at the beginning
def greet():
    talk(f"Hi {name}. I hope you are doing well. What do you need me to do?")

# Define a function that takes our input from defined earlier function and does various things, depending on what we told the bot to do
def run_bot():
    query = take_command()
    
    if any(i in query for i in ['have a good day', 'bye', 'goodbye', 'see you later', 'stop']):
        talk(f'Have a good day {name}!')
        exit()
    
    elif 'play music' in query:
        song = query.replace('play music', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        talk("Is there anything else I could do for you?")
    
    elif 'google' in query:
        google = query.replace('google', '')
        talk(f'searching {google} in google')
        pywhatkit.search(google)
        talk("Is there anything else I could do for you?")
    
    elif 'what is' in query:
        thing = query.replace('what is', '')
        talk(f'searching {thing} in wikipedia')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
        talk("Is there anything else I could do for you?")
    
    elif 'joke' in query:
        talk(pyjokes.get_joke())
        talk("Is there anything else I could do for you?")
    
    else:
        talk("I didn't understand that. Could you say that again?")
    
# Use our greeting function
greet()

# Run a bot until we tell him to stop
while True:
    run_bot()
