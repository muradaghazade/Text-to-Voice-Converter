from gtts import gTTS
from playsound import playsound

audio = 'voice.mp3'
language = 'en'
textt = input()
sp = gTTS(text=textt, lang=language, slow=False)

sp.save(audio)
playsound(audio)