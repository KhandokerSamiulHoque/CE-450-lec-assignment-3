def fltn(ls):
    flat_list = []
    try:
        flat_list = [item for sublist in ls for item in sublist] if any(isinstance(element, list) for element in ls) else ls
        return flat_list
    except Exception as e:
        print("An error occurred:", str(e))
        return flat_list

try:
    user_input = input("Enter the list of elements: ")
    elements = [eval(item) for item in user_input.split()]
    result = fltn(elements)
    print(result)
except Exception as e:
    print("Error!! :", str(e))