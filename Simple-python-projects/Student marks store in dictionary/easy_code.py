#---------- Students marks store in dict ---------#

## variables
count = 1
h_mark = -1
h_mark_name = ""
dict_list = {}

## starting the loop
while count < 4:
    name = input(f"Enter the student{count} name: ")   ### other inputs
    mark = int(input(f"Enter the {name}'s marks: "))

    dict_list[name] = mark   ### adding other values to dict

    
    if mark > h_mark:   ### finding the highest mark
        h_mark = mark
        h_mark_name = name

    
    count = count + 1

print(dict_list)
print()
print(f"Congratulations {h_mark_name}!! You got {h_mark}!!")
