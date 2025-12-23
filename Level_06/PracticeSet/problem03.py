# A spam comment is defined as a text containing following keywords: 
# "Make a lot of money", "Buy Now", "Subscribe This", "Click This". Write a program to detect these spams.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"


msg = input("Enter your comment: ")
msg = msg.lower()

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("Spam Comment...")
else:
    print("Not a Spam comment.")