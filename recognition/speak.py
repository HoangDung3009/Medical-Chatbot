import pyttsx3


def Say(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 180)
    print(f"Ciri: {Text}")
    engine.say(text=Text)
    engine.runAndWait()

