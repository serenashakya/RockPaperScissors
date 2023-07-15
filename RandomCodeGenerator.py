import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()"
numbers = "1234567890"

print("Print the length:")
length = int(input())

string = lower + upper + symbols + numbers
code = "".join(random.sample(string,length))

print("Your code is: ")
print(code)