a = int(input("Enter you age: "))
#start
if(a%2==0):
    print(f"{a} is even")

# end 

# start 
if(a>=18):
    print("Adult")
elif(a < 0):
    print("Entered invalid age")
else:
    print("Minor")

# end 

print("End of the program")