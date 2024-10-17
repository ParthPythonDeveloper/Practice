# Write a program to find out whether a given post is talking about “Parth” or not

post = input("Enter the post: ")

if("Parth".lower() in post.lower()):
    print("THis is post is right")
else:
    print("This is wrong")