from datetime import datetime
from gtts import gTTS
from os import remove
from playsound import playsound
from datetime import datetime


def say_hello():
    obj = gTTS(text='Привет!!!', lang='ru', slow=False)
    obj.save('sound.mp3')
    playsound('sound.mp3')
    remove("sound.mp3")


def say_time():
    d = datetime.now().strftime('%H:%M')
    obj = gTTS(text=f'Сейчас {d}', lang='ru', slow=False)
    obj.save('sound.mp3')
    playsound('sound.mp3')
    remove("sound.mp3")
