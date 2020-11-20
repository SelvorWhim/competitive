# assumes incomingcall, connect and hangup will be called in sequence

class Phone:
    caller = ""
    ring = ""
    screen = ""
    microphone = ""

    def incomingcall(self, num_calling):
        # doing this lookup every time is inefficient, but necessary because contacts changes during tests
        self.caller, self.ring = next(((contact["name"], contact["ring"]) for contact in contacts if contact["number"] == num_calling), ("stranger", "Di Da Di"))
        self.screen = f"Call: {self.caller}\nNumber: {num_calling}"
    
    def connect(self):
        self.screen = ""
        self.ring = ""
        if self.caller == "stranger":
            self.microphone = "Hello, who is speaking, please?"
        else:
            self.microphone = f"Hello, {self.caller}!"
    
    def hangup(self):
        self.microphone = ""
