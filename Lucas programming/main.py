# from magic_eight_ball import get_eight_ball_response
# question = input ("Ask the Magic Eight Ball a question: ")

# try:
#     if not question.strip():
#         raise ValueError("question can not be empty")
#     answer = get_eight_ball_response()
#     print (f"\n Magic Eight Ball Says: {answer}")
# except ValueError as error:
#     print(f"Input error: {error}")

# balance = 500.00

# print("Welcome to the class Bank")

# while True:
#     print("\n1. Check balance")
#     print("2. Deposit money")
#     print("3. Withdraw money")
#     print("4. Exit")

#     option = input("Choose an option: ")

#     match option:
#         case "1":
#             print(f"Your balance is €{balance:.2f}")

#         case "2":
#             try:
#                 amount = float(input("Enter amount to deposit: €"))

#                 if amount <= 0:
#                     raise ValueError("Amount must be greater than zero")

#                 balance += amount

#                 print("Deposit successful")
#                 print(f"New balance: €{balance:.2f}")

#             except ValueError as error:
#                 print("Error:", error)

#         case "3":
#             try:
#                 amount = float(input("Enter amount to withdraw: €"))

#                 if amount <= 0:
#                     raise ValueError("Amount must be greater than zero")

#                 balance -= amount

#                 print("Withdraw successful")
#                 print(f"New balance: €{balance:.2f}")

#             except ValueError as error:
#                 print("Error:", error)

#         case "4":
#             print("Exit")
#             break 

print("Temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

option = input("Choose an option: ")

try:
    temperature = float(input("Enter the temperature: "))

    match option:
        case "1":
            result = (temperature * 9 / 5) + 32
            print(f"{temperature} C = {result:.2f} F")

        case "2":
            result = (temperature - 32) * 5 / 9
            print(f"{temperature} F = {result:.2f} C")

        case "3":
            result = temperature + 273.15
            print(f"{temperature} C = {result:.2f} K")

        case _:
            print("Invalid option")

except ValueError as error:
    print("Error:", error)
