# Write a program to find out whether a given post is talking about "shanaya" or not.
post = input("Enter your post: ")

if("Shanaya".lower() in post.lower()):
    print("This post is talking about shanaya")
else:
    print("This post is not talking about shanaya")