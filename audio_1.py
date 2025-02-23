from gtts import gTTS
audio="speech.mp3"
language='en'
sp=gTTS(text="hi sailu,how are you",lang=language,slow=False,tld="com.au")
sp.save("tex.mp3")