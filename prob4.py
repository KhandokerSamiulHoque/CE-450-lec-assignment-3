def f(suits, numbers):
    suit_no = []
    try:
        if not suits or not numbers:
            return suit_no
        else:
            suit_no = [[suit, number] for suit in suits for number in numbers]
            return suit_no
    except Exception as e:
        print("Error!!:", str(e))
        return suit_no

try:
    suits = input("Enter a list of suits : ").split()
    numbers = [int(num) for num in input("Enter a list of numbers: ").split()]

    output = f(suits, numbers)
    print(output)
except ValueError:
    print("Invalid input. Please enter valid suits and numbers.")
