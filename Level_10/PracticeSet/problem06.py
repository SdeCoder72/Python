# Can you change the self parameter inside a class to something else (say "shanaya"). Try changing self to slf or shanaya and see the effects
# Write a class Train which has methods to book a ticket, get status(no of seats) and get fare info of train running under Induan Railways.
from random import randint
class Train:
    def __init__(slf, trainNo):  # no error
        slf.trainNo = trainNo

    def book(shanaya, fro, to):
        print(f"Ticket is booked in train no: {shanaya.trainNo} from {fro} to {to}")  #output intact

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on Time")

    def fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(333, 666)}")

t = Train(12345)
t.book("Madhupur", "Delhi")
t.getStatus()
t.fare("Dhanbad", "Delhi")
