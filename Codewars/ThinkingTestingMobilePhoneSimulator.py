# assumes incomingcall, connect and hangup will be called in sequence
# partial solution: convert_contacts doesn't work for full tests because some of them change contacts after creating the Phone object

class Phone:
    caller = ""
    ring = ""
    screen = ""
    microphone = ""
    contact_dict = {} # maps number to tuple of name and ring
    
    def __init__(self):
        self.convert_contacts(contacts)
    
    def convert_contacts(self, unconverted_contacts):
        for contact in unconverted_contacts:
            self.contact_dict[contact['number']] = (contact['name'], contact['ring'])

    def incomingcall(self, num_calling):
        self.caller, self.ring = self.contact_dict.get(num_calling, ("stranger", "Di Da Di"))
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
