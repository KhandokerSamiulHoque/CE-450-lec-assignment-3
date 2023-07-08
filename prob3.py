def add_many(x, elem, lst):
    try:
        count = lst.count(x)
        lst.extend([elem] * count)
    except ValueError:
        print(f"The elemement {x} is not found in the list.")

lst = []
try:
    lst = [int(num) for num in input("Enter the list of numbers: ").split()]
    x = int(input("Enter element to search : "))
    elem = int(input("Enter element to add : "))

    add_many(x, elem, lst)
    print(lst)
except ValueError:
    print("Wrong Input, Enter the number !!")