import pyttsx

class voice :

    def __init__(self):

        self.engine = pyttsx.init()


    def say(self, string):
        self.engine.say(string)
        self.engine.runAndWait()

    def reset(self):
        self.engine = pyttsx.init()
