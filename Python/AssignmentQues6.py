#6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome



string = input("Enter the string")

Rev_str = string[::-1]
print(Rev_str)

if (string == Rev_str):
    print("palindrome")
else:
    print("not a palindrome")
