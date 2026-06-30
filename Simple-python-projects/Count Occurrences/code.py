#------------------ Read the list and count -----------------------------------#

## the list
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

## variables with value for use
count = 0
apple = 0
banana = 0
orange = 0

while count < 6:   ## starting the loop
    if fruits[count] == "apple":   ## start checking items on list
        apple = apple + 1   ## store value in variables if the condition is true

    if fruits[count] == "banana":
        banana = banana + 1

    if fruits[count] == "orange":
        orange = orange + 1 
    
    count = count + 1
    
## print output
print(f"apple: {apple}")
print(f"banana: {banana}")
print(f"orange: {orange}")
