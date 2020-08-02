
import pyttsx3 as tts
s=tts.init()
s.say("Text nvgfhjd  ghjg")
s.runAndWait()
'''
from gtts import gTTS
import os
txt1=input('enter:')
tts=gTTS(text=txt1)
tts.save('aa.mp3')
os.system("mpg321 aa.mp3")


from win32api.client import Dispatch
s=Dispatch("SAPI.SpVoice")
s.Speak('Text')
'''
