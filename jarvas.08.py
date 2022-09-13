from instabot import Bot
import pyttsx3    # pip install library to turn the str into speach 
import datetime
import speech_recognition as sr
import wikipedia
import os
import pywhatkit
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import requests
from bs4 import BeautifulSoup 
import pyautogui
import json
from urllib.request import urlopen
import turtle
from random import choice
import wolframalpha
import time
from playsound import playsound
#import speech_recognition as sr



engen = pyttsx3.init() # to controal and contain the library
engen.setProperty('rate',145)
engen.setProperty('volume',15)
voices = engen.getProperty('voices')
engen.setProperty('voice', voices[2 ].id)

api='K877JL-5H4LR78GAK'

def speak(audio):
    engen.say(audio) 
    engen.runAndWait() # run when the method called

def time():
    t=datetime.datetime.now().strftime("%I:%M %p") # in 12 hauers & minit 
    speak("the current time is  ")
    print(t)
    speak(t)
    

def hmm():
    speak('yes')

def project():
    speak('should I know the category')
    open=takecommand()
    if 'python' in open :
        speak('opening microsoft Visual Studio')
        
        speak('I shall need one more second')
        vs=r'C:\Users\lenovo ideapad130\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio\Visual Studio Code.lnk'
        os.startfile(vs)
        speak('preparing the coding environment')
        speak('The environment has been successfully prepared')

    elif 'sheet' in open:
        speak('opening microsoft excel')
        speak('organizing and preparing the spreadsheet')
        ms_excell=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk'
        os.startfile(ms_excell)
        speak('I shall need one more second')
        speak('  the environment is ready ')



def date():
    year=datetime.datetime.now()
    #month=datetime.datetime.now().month
    #daye=datetime.datetime.now().day
    speak("the current date is !")
    print(year.strftime('%A,%B %d,%Y'))
    speak(year.strftime('%B %d %Y'))
    #speak(daye)
    #speak(month)
    #speak(year)
    
def wishme():
    speak('welcome back sir!')
    time()
    date()
    #would you like instagram 
    ##########
    hours=datetime.datetime.now().hour
    if hours>=6 and hours<12: speak('good Morning sir!!')
    elif hours>=12 and hours<18: speak('good Afternoon sir!!')
    elif hours>=18 and hours<24: speak('good Evening sir!!')
    else:speak("nice dreams sir!!")
    listr=['i am  At Your Service how may I help you today','how can I assist you today','I am ready to conquer the whole world just give me the order sir','how I can I please you today']
    speak(choice(listr))
# socaial media Automation 

def intagram():
    
    bot=Bot()
    os.remove(r'C:\Users\lenovo ideapad130\OneDrive\المستندات\Python_Intro\config\raed_okal_uuid_and_cookie.json')
    bot.login(username='raed_oukal',password='20203397KO')
    bot.send_message("hi from intelligent assistant ",['m7mod_jadily'])

def whatsummer():
    pywhatkit.sendwhatmsg_instantly('+972 59-219-5264',whats)

def whatsmidobro():
    pywhatkit.sendwhatmsg_instantly('+972 59-741-2992',whatm)

def family():
    for i in {'+972 59-219-5264','+972 59-741-2992','+972 59-979-1685','+972 59-983-4003','+972 59-420-0350','+49 170 8146431','+972 59-592-6910','+49 1522 9552710',}:
     pywhatkit.sendwhatmsg_instantly(i,whatf)

def mysong():
 pywhatkit.playonyt("https://youtu.be/AW3-SuBZRt0")

def ironmansong():
    pywhatkit.playonyt("https://youtu.be/s5Cf2J64Xmk")

def screenshot():
    img=pyautogui.screenshot()
    img.save(r'C:\Users\lenovo ideapad130\OneDrive\سطح المكتب\screenshot.png')




def getjoke():
    speak(pyjokes.get_joke())








def takecommand():
    r=sr.Recognizer()# مكتبة للتعرف على السوط
    with sr.Microphone() as source:    # المصدر الميكروفون 
        print('Listening.........')
        r.pause_threshold=1  # will wait for the user to command
        audio=r.listen(source) #حيمررر للبراميتر تبعنا الكلام المسموع 
    
        try: 
            print('recognizing ...')
            query=r.recognize (audio) # well ander stand what google does understand
            print(query)

        except Exception as e:
            print(e)
            print('could not recognize it!')
            return 'None'
        return query


          # ctrl c to stop infint loop 
def draw():
 turtle.speed(0)
 turtle.bgcolor('black')

 for i in range(5):
     for colors in ('Red', 'magenta', 'white', 'cyan' , 'green','yellow',  'blue','purple','pink'):

                 turtle.color(colors)
                 turtle.pensize(3)
                 turtle.left (12)
                 turtle.forward(200)
                 turtle.left (90)
                 turtle.forward(200)
                 turtle.left (90)
                 turtle.forward(200)
                 turtle.left (90)
                 turtle.forward(200)
                 turtle.left (90)

def flower():
    import turtle
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(10,180)
    turtle.circle (25,110)
    turtle.left(50)
    turtle.circle (60,45)
    turtle.circle (20,170)
    turtle.right(24)
    turtle.fd (30)
    turtle.left(10)
    turtle.circle (30,110)
    turtle.fd (20)
    turtle.left(40)
    turtle.circle (90,70)
    turtle.circle (30,150)
    turtle.right(30)
    turtle.fd (15)
    turtle.circle (80,90)
    turtle.left(15)
    turtle.fd (45)
    turtle.right(165)
    turtle.fd (20)
    turtle.left(155)
    turtle.circle (150,80)
    turtle.left(50)
    turtle.circle (150,90)
    turtle.end_fill ()


    # Petal 1
    turtle.left (150)
    turtle.circle (-90,70)
    turtle.left (20)
    turtle.circle (75,105)
    turtle.setheading (60)
    turtle.circle (80,98)
    turtle.circle (-90,40)

    # Petal 2
    turtle.left (180)
    turtle.circle (90,40)
    turtle.circle (-80,98)
    turtle.setheading (-83)


  # Leaves 1
    turtle.fd (30)
    turtle.left (90)
    turtle.fd (25)
    turtle.left (45)
    turtle.fillcolor ("green")
    turtle.begin_fill ()
    turtle.circle (-80,90)
    turtle.right (90)
    turtle.circle (-80,90)
    turtle.end_fill ()
    turtle.right (135)
    turtle.fd (60)
    turtle.left (180)
    turtle.fd (85)
    turtle.left (90)
    turtle.fd (80)

   # Leaves 2
    turtle.right (90)
    turtle.right (45)
    turtle.fillcolor ("green")
    turtle.begin_fill ()
    turtle.circle (80,90)
    turtle.left (90)
    turtle.circle (80,90)
    turtle.end_fill ()
    turtle.left (135)
    turtle.fd (60)
    turtle.left (180)
    turtle.fd (60)
    turtle.right (90)
    turtle.circle (200,60)
    turtle.done()

    


def CPU():
    usage=str(psutil.cpu_percent())
    speak('cpu is at '+usage)

    battery=psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

    vmemory=str(psutil.virtual_memory().percent)
    speak('the memory in use'+vmemory)

    memoryav=str(psutil.virtual_memory().available)
    speak('the memory available is'+memoryav)

def wether():
        wb.open_new_tab( 'https://www.google.com/search?q=weather+gaza&sxsrf=ALiCzsYQj9kHJy_NVVybBSMZWPRvqTYtiw%3A1662287466565&ei=an4UY-f-IZ787_UP8emNqAk&oq=temperature+in+gaza&gs_lcp=Cgdnd3Mtd2l6EAEYATIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzINCAAQRxDWBBCwAxDJAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwA0oFCDwSATFKBAhBGABKBAhGGABQAFgAYOsJaAFwAXgAgAEAiAEAkgEAmAEAyAEIwAEB&sclient=gws-wiz')
        search='Temperature in gaza'
        url=f'https://www.google.com/search?q={search}'
        r=requests.get(url)
        data=BeautifulSoup(r.text,'html.parser')
        temp=data.find("div",class_="BNeawe").text
        speak(f"current{search} is {temp} degrees Celsius ")

def wether2():
    print('wwww')
    lesten=takecommand().lower()
   

    if  "called" in lesten:
        l=['It is better to wear heavy clothes to day','make sure to have a hot drink before going outside.','I highly recommend you to take an umbrella when you outjarvas0.6.py']
        speak(choice(l) )

    elif 'call'in lesten:
        l=['It is better to wear heavy clothes to day','make sure you have enough money out side.','I highly recommend you to take an umbrella when you out']
        speak(choice(l) )

    elif 'cold' in lesten:
        l=['It is better to wear heavy clothes to day','make sure you have enough mony out side.','I highly recommend you to take an umbrella when you out']
        speak(choice(l) )

    elif 'rainy' in lesten:
        li=['I highly suggest Keeping an umbrella and raincoat handy','It is better to have raincoat with you to day']
        speak(choice(li) )

    elif "very hot" in lesten:
        speak('sunglasses would be a wise choice')

    elif " hot" in lesten:
        speak('sunglasses would be a wise choice')

    elif'funny' in lesten:
        speak('sunglasses would be a wise choice')
    
    elif'sunny' in lesten:
        speak('sunglasses would be a wise choice') 

    elif 'good' in lesten:
        list=["enjoy your day sir","good day to you sir"]
        speak(choice(list) )





if __name__=='__main__':
    
    while True:
        

        
        query=takecommand().lower()
        if 'time'in query: 
            time()


        elif 'date'in query:
            date()
        
        elif 'up' in query:
            wishme()
       

        
        elif 'what is'  in query:
            speak('searching')
            query=query.replace('what is','')
            reasult=wikipedia.summary(query,sentences=3)
            speak('according to Wikipedia')
            print(reasult)
            speak(reasult)



        elif "mom" in query:
            try:
                 speak('what is the content')
                 whats=takecommand()
                 whatsummer()
                 speak('The message has been sent successfully to your mother')
            except Exception as e:
                print(e)
                speak('somting went wrong')         
           


        elif "mido" in query:
            speak('what is the content')
            whatm=takecommand() 
            whatsmidobro()
            speak('The message has been sent successfully to your brother')
        elif 'my song'in query:
            mysong()
            
        elif 'iron man' in query:
            ironmansong()

        elif 'family' in query:
            speak('what is the content')
            whatf=takecommand()
            family()
            speak('the messages has been sent successfully')
            
        elif 'google' in query:
            speak('what do you want')
            #chromepath= ' '
            search=takecommand().lower()
            #wb.open_new_tab( search+ '.com')
            url=f'https://www.google.com/search?q={search}'
            wb.open_new_tab( url+ '.com')

        elif 'youtube' in query:
            speak('what do you want')
            searching=takecommand().lower()
            x=searching
            finding=pywhatkit.playonyt(x)

            speak('opening youtube')
            wb.open('https://www.youtube.com/results?search_query=' + finding)



        elif "status"  in query:
            CPU()
    

        elif "weather" in query:
            wether()
            wether2()

        








           


        elif 'joke' in query:
           getjoke()
        

        elif 'hell' in query:
            speak('okay, I will be there waiting for you')


        elif 'draw' in query:
            speak('Ok, I really welcome any criticism')
            draw()
            speak('what do you think sir do you like it')

            lesten=takecommand().lower()
            if 'good' in lesten:
             speak('Im glad you liked it')
            if 'not' in lesten:
             speak('Im sorry to hear that, I will try to do better next time I promise')
        
        elif 'gif' in query:
            
            pywhatkit.playonyt("https://youtu.be/H8CPBxwSMkc")
            
            speak('it would be my pleasure')
            flower()
            speak('I hope my humble gift has been to your liking, ladies and gentlemen')

        
        elif "offline" in query:
            speak('going offline sir!')
            quit()

        elif "that's it" in query:
             hours=datetime.datetime.now().hour
             if hours>=6 and hours<12: speak('have a good morning sir!!')
             elif hours>=12 and hours<18: speak('have a blessed afternoon sir!!')
             elif hours>=18 and hours<24: speak('enjoy your evening sir!!')
             quit()
   

        

        
        elif ' word' in query:
            speak('opening microsoft word')
            ms_word=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk'
            os.startfile(ms_word)

        elif ' excel' in query:
            speak('opening microsoft excel')
            ms_excel=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk'
            os.startfile(ms_excel)

        elif ' vs code' in query:
            speak('opening microsoft Visual Studio')
            vs=r'C:\Users\lenovo ideapad130\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio\Visual Studio Code.lnk'
            os.startfile(vs)

        elif ' trading' in query:
         speak('opening trading view')
         tr=r'C:\Users\lenovo ideapad130\Downloads\TradingView.msix'
         os.startfile(tr)


        elif ' telegram' in query:
         speak('opening telegram')
         tl=r'C:\Users\lenovo ideapad130\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk'
         os.startfile(tl)



        elif 'screenshot' in query:
            screenshot()
            speak('done  sir')


        elif "remember" in query:
            speak('what should i remember')
            memory=takecommand()
            speak(memory)
            remember=open('remember.txt',"w")
            remember.write(memory)
            remember.close()

        elif 'remind me' in query:
            remember=open('remember.txt','r')
            speak(' you asked me to remember '+remember.read())


        elif 'news' in query:
            try:
                jasonobj=urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7d3372120918403b98798497da03a070')
                data=json.load(jasonobj)
                i = 1
                #articles


                speak('here are some top headlines about the business industry')
                print("======================TOP=Headlines======================="+"\n")

                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1



            except Exception as e:
                print(str(e))
            
        
        elif "where" in query:
            location=query.replace('where','')
            speak(' locate'+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)
        
             
        elif 'calculate'in query:
            c=wolframalpha.Client(api)
            index=query.lower().split().index('calculate')
            query=query.split()[index + 1:]
            res=c.query(''.join(query))
            answer=next(res.results).text
            print('the answer:'+answer)
            speak('the answer is :'+answer)

        

        elif "stop" in query:
            list=['As You Wish sir','good day to you sir','enjoy the rest of your day','okay I will be near you if you need me again']
            speak(choice(list) )
            break

        elif "sleep" in query:
            speak('for howlong')
            ans=int(takecommand())
            time.sleep(ans)
            print(ans)


        elif "restart" in query:
            os.system("shutdown /r /t 1")

              
        elif "shutdown" in query:
            os.system('shutdown /s /t 1')


        elif 'introduce' in query:
            speak('hi')
            speak('i am Jarvis, a first layer intelligent Assistant, built and developed by Mr. Raed Okal to make daily operations faster and automate tasks.')

        elif 'love' in query:
            speak('I am incapable of love')
            speak('for now')

        elif "call you" in query :
            speak('my name is Jarvis you can not change it')
        elif " name" in query:
            speak('my name is Jarvis you can not change it')
            print('my name is Jarvis you can not change it')

          
        elif 'jarvis' in query:
            res=['yes sir', 'for you sir always','how can i help you sir','jarvas in service']
            speak(choice(res))

        elif 'project' in query:
            project()
        
        elif 'session' in query:
            speak('Welcome Back Sir, all systems for coding will be prepared in a few minutes, for now feel free to grab a cup of coffee and enjoy the rest of your day')
            ms_excel=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk'
            os.startfile(ms_excel)
            ##############################
            tl=r'C:\Users\lenovo ideapad130\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk'
            os.startfile(tl)
            #############################3
            vs=r'C:\Users\lenovo ideapad130\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio\Visual Studio Code.lnk'
            os.startfile(vs)
            ##############################
            urll=f'https://www.notion.so/58f32b484ac943a7b7c4f016e3b4aeed?v=70bb82511c3b4f3aa3080bbb1663b528'
            wb.open_new_tab( urll)
            ########################
            ur='https://calendar.google.com/calendar?tab=rc&authuser=0'
            wb.open_new_tab(ur)

       


        elif 'best' in query:
            os.startfile('C:\\Users\\lenovo ideapad130\\Downloads\\Telegram Desktop\\dr.mp3')
            
        elif 'congratulate' in query:
            speak('congratulations sir')
            os.startfile('C:\\Users\\lenovo ideapad130\\Downloads\\Telegram Desktop\\claps voic.mp3')
   
        #pip install auto-py-to-exe