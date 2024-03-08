print("Hello! My name is blackmamba.")
print("I was created in 2024.")
print('Please, remind me your name.')
owner_name = input("Enter your name: ")
# reading a name
print(f"What a great name you have, {owner_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("remainder of dividing3 :"))
remainder5 = int(input("remainder of dividing5 :"))
remainder7 = int(input("remainder of dividing7 :"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
