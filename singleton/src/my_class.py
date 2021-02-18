class SaySomething:

    def __init__(self, message):
        self.message = message

    def say(self):
        print(self.message)

    def change_message(self, new_message):
        self.message = new_message
