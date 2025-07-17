import gtts
text = input("Enter something here::")

sound = gtts.gTTS(text,lang='en')

sound.save("output.mp3")
playsound.playsound("output.mp3")
