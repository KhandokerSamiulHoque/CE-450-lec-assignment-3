def chk_elm(lst, n):
    try:
        for element in lst:
            if isinstance(element, list):
                if chk_elm(element, n):
                    return True
            elif element == n:
                return True
        return False
    except Exception as e:
        print("An error occurred:", str(e))
        return False

try:
    user_input = input("Enter the list of elements : ")
    elements = [eval(item) for item in user_input.split()]
    findings = eval(input("Enter the target element to search for: "))

    Output = chk_elm(elements, findings)
    print(Output)
except Exception as e:
    print("An error occurred:", str(e))
