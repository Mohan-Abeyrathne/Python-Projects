#---------- Students marks store in dict ---------#

### 1'st input
name = input(f"Enter the student1 name: ")
mark = int(input(f"Enter the {name}'s marks: "))

## variables
count = 2
dict_list = {}
h_mark = mark
h_mark_name = name

dict_list[name] = mark   ### adding 1'st value to dict

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
