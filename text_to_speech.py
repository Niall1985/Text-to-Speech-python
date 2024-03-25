import pyttsx3
text_to_speech = pyttsx3.init()
text_to_convert = input("Enter the text which you wish to convert to speech:")
text_to_speech.say(text_to_convert)
text_to_speech.setProperty('rate',100)
text_to_speech.runAndWait()