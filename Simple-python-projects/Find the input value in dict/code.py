marks = {"Alice": 85, "Bob": 90, "Charlie": 85}

mark2 = int(input("Enter marks: "))

list = []

for name, mark in marks.items():
    if mark2 == mark:
        list.append(name)

if list:
    
