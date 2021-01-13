import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import re
# from weather import Weather

# sapi5 api h
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
      speak("Good Evening")

    speak("I am Venus Please tell me how may I help you")

def takeCommand():
        # It takes microphone input from the user and returns string output
        #yeh sb speech regonition module se aaya h
     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)


     try:
         print("Recognizing.......")
         query=r.recognize_google(audio,language='en-in')
         print(f"User said: {query}\n")

     except Exception as e:
         print("Say that again please") 
         return "None"
     return query      


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tanudahiya18@gmail.com','dahiya123')
    server.sendmail('tanudahiya18@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
          query=takeCommand().lower()
      
          #logic for executing tasks based on query
         
          if 'wikipedia' in query:
                    speak('Searching Wikipedia')
                    query=query.replace("wikipdedia","")
                    results=wikipedia.summary(query,sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

          elif 'open youtube' in query:
              webbrowser.open('youtube.com') 

          elif 'open google' in query:
              webbrowser.open('google.com')     

          elif 'open stack overflow' in query:
              webbrowser.open('stackoverflow.com')

          elif 'open udemy' in query:
              webbrowser.open('udemy.com')

          elif 'open netflix' in query:
              webbrowser.open('netflix.com')

          elif 'open spotify' in query:
              webbrowser.open('spotify.com')

          elif 'open cricbuzz' in query:
              webbrowser.open('cricbuzz.com')

          elif 'play music' in query:
              music_dir='C:\\Swasti\\sems\\3rd yr project\\Songs'
              songs=os.listdir(music_dir)
              print(songs)
              os.startfile(os.path.join(music_dir,songs[0]))
      
          elif 'the time' in query:
              strTime=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"The time is {strTime}")

          elif 'open visual studio code' in query:
                codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

          elif 'open downloads' in query:
                codePath="C:\\Users\\DELL\\Downloads"
                os.startfile(codePath)
            
          elif 'open notepad' in query:
                codePath="C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                os.startfile(codePath)

          elif 'stop listening' in query:
                speak("Quitting Venus!")
                break

          elif 'open command prompt' in query:
                codePath="C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
                os.startfile(codePath)

          elif 'open website' in query:
                reg_ex = re.search('open website (.+)', query)
                if reg_ex:
                    domain = reg_ex.group(1)
                    url = 'https://www.' + domain
                    webbrowser.open(url)
                    print('Done!')
                else:
                    pass

          elif 'how\'s you doing'  in query:
                speak('Just doing my thing')
                
          elif 'Good job'  in query:
                speak('Thank you')


        #   elif 'current weather in' in command:
        #         reg_ex = re.search('current weather in (.*)', command)
        #         if reg_ex:
        #             city = reg_ex.group(1)
        #             weather = Weather()
        #             location = weather.lookup_by_location(city)
        #             condition = location.condition()
        #             talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

          elif 'send email to me' in query:
              try:
                  speak('What should I say?')
                  content=takeCommand()
                  to="swastidahiya18@gmail.com"
                  sendEmail(to,content)
                  speak("Email has been sent!")
              except Exception as e:
                  print(e)
                  speak("Sorry Mam!I am not able to send this email")
                           
