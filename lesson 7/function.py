def greeting():
    print("Hello, world!")

def greeting_with_tone(tone: str):
    tone = tone.lower()
    if tone == "happy":
        print("hiii :)")
    elif tone == "normal":
        print("Hi!")
    else:
        print("What's up!")