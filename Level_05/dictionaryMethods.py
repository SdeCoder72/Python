studentMarks = {
    "Shanaya" : 98,
    "Anaya" : 76,
    "Neha" : 86,
    9 : "Kavya",
}

print(studentMarks.items())
print(studentMarks.keys())
print(studentMarks.values())
studentMarks.update({"Shanaya": 95})  #updated shanaya's value
print(studentMarks)  # changed the original dictionary
studentMarks.update({"Shivam": 75})  # creates one key-value in the end
print(studentMarks)

print(studentMarks.get("Shanaya"))
print(studentMarks["Shanaya"])

print(studentMarks.get("Shanaya2"))  # returns None
# print(studentMarks["Shanaya2"])  # ERROR

d1 = {
    1 : "a",
    2 : "b",
    3 : "c"
}

print(d1)
d1.clear()
print(d1)

studentMarks.pop("Shivam", )
print(studentMarks) 
print(len(studentMarks)) 
