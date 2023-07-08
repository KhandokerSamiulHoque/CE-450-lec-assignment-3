def sym(l):
    try:
        return l == l[::-1]
    except Exception as e:
        print("An error occurred:", str(e))
        return False

try:
    user_input = input("Enter a list of elements (separated by spaces): ")
    elements = [eval(item) for item in user_input.split()]

    output = sym(elements)
    print(output)
except Exception as e:
    print("An error occurred:", str(e))