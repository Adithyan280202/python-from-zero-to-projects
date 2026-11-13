
# Mini Project 09: Multiplication Table Generator

print("===================================")
print("     MULTIPLICATION TABLE GENERATOR")
print("===================================")

choice = "yes"

while choice == "yes":

    number = int(input("\nEnter the number: "))
    start = int(input("Enter the starting multiplier: "))
    end = int(input("Enter the ending multiplier: "))

    total = 0

    print("\nMultiplication Table")
    print("-----------------------------")

    for i in range(start, end + 1):

        result = number * i

        print(f"{number} x {i} = {result}")

        total = total + result

    print("-----------------------------")
    print("Total of all results:", total)

    choice = input("\nDo you want to generate another table? (yes/no): ").lower()

print("\nThank you for using the Multiplication Table Generator!")
