marks = {
    "Parth": 100,
    "rushit": 90,
    "PS": 80,
}
print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
# marks.update({"Parth":99,"zalak":90})
print(marks)

print(marks.get("Parth2")) # Prints None
print(marks["Parth2"]) # Returns an error