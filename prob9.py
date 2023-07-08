from operator import add, sub, mul
def fld(lst, g, m):
    try:
        if len(lst) == 0:
            return m
        else:
            m = g(m, lst[0])
            lst = lst[1:]
            return fld(lst, g, m)
    except Exception as e:
        print("An error occurred:", str(e))
        return m


try:
    user_input = input("Enter a list of numbers (separated by spaces): ")
    s = [eval(num) for num in user_input.split()]

    result_sub = fld(s, sub, 0)
    print(result_sub)

    result_add = fld(s, add, 0)
    print(result_add)

    result_mul = fld(s, mul, 1)
    print(result_mul)

    result_blank = fld([], sub, 100)
    print(result_blank)

except Exception as e:
    print("An error occurred:", str(e))
