def removechar(string, x, y):
    first = string.replace(x,'')
    result = first.replace(y,'')
    return result
string = input("Enter a string: ")
x= input("Enter the character to remove: ")
y= input("Enter the character to remove: ")

result = removechar(string, x, y)
print(f"String after removing '{x}','{y}' : {result}")
print(result[::-1])


