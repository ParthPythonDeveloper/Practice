f = open("file.py")

print(f.read())
f.close()

with open("file.py") as f:
    print(f.read())