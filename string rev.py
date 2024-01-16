def removechar(string, x, y): #defining the function
    first = string.replace(x,'')
    result = first.replace(y,'')
    return result #returning the resultant string
string = input("Enter a string: ")
x= input("Enter the character to remove: ") #taking the inputs from user
y= input("Enter the character to remove: ")

result = removechar(string, x, y) #calling the function
print(f"String after removing '{x}','{y}' : {result}")
print(result[::-1])


