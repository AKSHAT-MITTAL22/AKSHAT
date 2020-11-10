import calendar
import datetime
import os
import random
import warnings
import wikipedia
import speech_recognition as sr
from gtts import gTTS

warnings.filterwarnings('ignore')
def recordAudio():
       r=sr.Recognizer()
       with sr.Microphone() as source:
         print('Say Something!')
         audio = r.listen(source)
       data = ''
       try:
         data =r.recognize_google(audio, lang='en-in')
         print('You said:'+data)
       except sr.UnknownValueError:
         print('Google Speech Recognition could not understand your audio , unknown error')
       except sr.RequestError as e:
         print('Request results from Google Speech Recognition service error' +e)
       return data
def assistantResponse(text):
    print(text)
    myobj = gTTS(text= text, lang='en', slow=False)
    myobj.save('assistant_response.mp3')
    os.system('start assistant_response.mp3')
def wakeWord(text):
    WAKE_WORDS=['hey computer','okay computer']
    text=text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    month_names=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21th','22th','23th','24th','25th','26th','27th','28th','29th','30th','31th']
    return 'Today is '+weekday+ ' , ' + month_names[monthNum-1]+' the '+ ordinalNumbers[dayNum-1]+' . '
def greeting(text):
    GREETING_INPUTS=['HEY','GREETINGS','HELLO']
    GREETINGS_RESPONSES=['Howdy','Whats Good','Hello','Hey There']
    for word in text.split():
        if word.upper() in GREETING_INPUTS:
            return random.choice(GREETINGS_RESPONSES)+'.'
    return ''
def getPerson(text):
    wordList=text.split()
    for i in range(0,len(wordList)):
        if i+3<=len(wordList)-1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is' :
           return wordList[i+2]+' '+ wordList[i+3]


while True:
    text=recordAudio()
    response= ''
    if(wakeWord(text)==True):
        response = response + greeting(text)
        if('date' in text):
            get_date=getDate()
            response=response+' '+get_date
        if('time' in text):
            now=datetime.datetime.now()
            meridian=''
            if now.hour >=12:
                meridian='p.m'
                hour=now.hour-12
            else:
                meridian='a.m'
                hour=now.hour
            if now.minute<10:
                minute='0'+str(now.minute)
            else:
                minute=str(now.minute)
            response=response+' '+str(hour)+':'+minute+' '+meridian+'.'
        if('who is' in text()):
            person=getPerson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response+' '+wiki
assistantResponse(response)
