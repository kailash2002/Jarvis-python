import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=9 or hour<12):
        speak("good morning")
    elif(hour>=12 or hour <18) :
        speak("good afternoon")
    else:
        speak("good evening") 
    speak("i am your jarvis sir,how may i help you!")
def takecommand() :
    #it takes microphone input from user and return string
    r=sr.Recognizer()   
    with sr.Microphone() as source:
        print("listening...")    
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...") 
        query=r.recognize_google(audio,language='en-in')  
        print(f"you said :{query}") 
    except Exception as e:
        print("say that again plaese")
        return "None"    
    return query    
             


if __name__== "__main__":
    wishme()
    while(True):
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak(" searching wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            speak("according to wikipedia....")
            speak(result)
        elif 'open youtube ' in  query:
            webbrowser.open("youtube.com")

   