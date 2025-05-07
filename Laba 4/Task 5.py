try:
    array = [1,2,3,4,5,6,7,8,9,0]
    print (array)
    index_num = int(input("Enter the index of the number 1:  "))
    num = array[index_num]
    index_num_2 = int(input("Enter the index of the number 2:  "))
    num2 = array[index_num_2]
    result = num / num2
    print(f"division = {result}")
except ValueError:
    print("It's not a number")
except ZeroDivisionError:
    print("You can't divide by zero.")
except IndexError:
    print("Incorrect index")