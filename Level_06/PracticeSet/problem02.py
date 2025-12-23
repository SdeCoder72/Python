# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

math = int(input("Enter Math marks: "))
chemistry = int(input("Enter chemistry marks: "))
physics = int(input("Enter physics marks: "))

total_Percentage = (math+chemistry+physics)/3

if(total_Percentage >= 33 and math >= 33 and physics>=33 and chemistry>=33):
    print("Paas: ", total_Percentage)
else:
    print("Fail: ", total_Percentage)