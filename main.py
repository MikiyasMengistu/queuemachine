from process import process1
from counter import counter1
from dictionaries import customers

count = 0
keep = "."

if __name__ == '__main__':
    while keep != "e" and count < 3:  # if the user enters 'e' the loop will be terminated
        id_num = input("enter your id: ")
        if id_num in customers:
            process1()
            keep = input("Are you sure to exit, y/n: ")
            if keep == "n":
                process1()
            else:
                break
            count = 0
        else:
            count += 1
            continue
    else:
        print("So many trials, come back after 5 sec")
        counter1(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
