import requests
from bs4 import BeautifulSoup
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# get user input for the text to be converted to speech
text = "HELLO"

# use the engine to convert the text to speech
engine.say(text)

# run the engine to play the speech
engine.runAndWait()
print("HELLO")
engine.say("HOW CAN I HELP YOU")
engine.runAndWait()
print("HOW CAN I HELP YOU")
print()
print()
ques=input("do you want speech recognition(yes/no)")
if  ques=="yes":
    import speech_recognition as sr

    # Create a recognizer object
    r = sr.Recognizer()

    # Define the microphone as a source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
    
        # Prompt user to speak
        print("Speak now")
    
        # Record audio
        audio = r.listen(source)
    
        try:
            # Recognize speech using Google Speech Recognition
            query = r.recognize_google(audio)
            print("You said: ",query)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said")
            query = input("WHAT YOU WANT TO KNOW")
        except sr.RequestError as e:
            print("Sorry, there was an error processing your request; {0}".format(e))
            query = input("WHAT YOU WANT TO KNOW")
else:

    # Define the search query
    query = input("WHAT YOU WANT TO KNOW")

engine.say("HERE ARE SOME OF THE RESULTS about  "+query)
engine.runAndWait()

# Construct the Google search URL
url = f"https://www.google.com/search?q={query}"

# Send a request to the URL and get the response
response = requests.get(url)

# Use BeautifulSoup to parse the response HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find all the search result links
links = soup.find_all("a")

# Loop through the links and print the title and URL of the top results
for link in links:
    # Get the link URL and title
    url = link.get("href")
    title = link.getText()
   
    # Filter out any non-Google search result links and print the top results
    if "/url?q=" in url and not "webcache" in url:
        # Extract the URL from the Google search result link format
        url = url.replace("/url?q=", "").split("&")[0]
       
        # Print the result title and URL
        print(title)
        print(url)
        print()

engine.say("Do you want to open it in google(yes or no)")
engine.runAndWait()
ques=input("Do you want to open it in google(yes/no)")

if ques=="yes":
    url = f"https://www.google.com/search?q={query}"
    import webbrowser


    webbrowser.open(url)
    

else:
    print()
