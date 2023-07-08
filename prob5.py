def mrg(ls1, ls2):
    mrg_frst = []
    try:
        one = 0
        two = 0

        while one < len(ls1) and two < len(ls2):
            if ls1[one] < ls2[two]:
                mrg_frst.append(ls1[one])
                one += 1
            else:
                mrg_frst.append(ls2[two])
                two += 1

        mrg_frst += ls1[one:] + ls2[two:]
        return mrg_frst
    except Exception as e:
        print("Error!!:", str(e))
        return mrg_frst


try:
    ls1 = [int(num) for num in input("Enter the 1st list of numbers : ").split()]
    ls2 = [int(num) for num in input("Enter the 2nd list of numbers: ").split()]

    Output = mrg(ls1, ls2)
    print(Output)
except ValueError:
    print("Invalid input. Please enter valid numbers.")