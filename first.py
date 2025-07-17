import gtts
text = input("enter something here:")

sound = gtts.gTTS(text,lang='en')

sound.save("output.mp3")
playsound.playsoud("output.mp3")
