def crte_2d_arr(rows, columns):
    try:
        TwoD_array = [["-"] * columns for _ in range(rows)]
        return TwoD_array
    except Exception as e:
        print("An error occurred:", str(e))
        return []

try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    Output = crte_2d_arr(rows, columns)
    print(Output)
except ValueError:
    print("Invalid input. Please enter only valid numbers.")
except Exception as e:
    print("An error occurred:", str(e))