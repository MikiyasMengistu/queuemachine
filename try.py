import time
import numbers1

turn = numbers1.queue_dict  # turn is dictionary that exists on numbers1' module. it consists of areas of drug stor as
                           # key and list of turn numbers1 as value
count = 0
areas = "."

while areas != "e" and count<3:  # if the user enters 'e' the loop will be terminated
    id_num = input("enter your id: ")
    if id_num in numbers1.customers:
        numbers1.process()
        keep = input("Do you wanna continue, y/n: ")
        if keep == "y":
            numbers1.process()
        else:
            continue
        count = 0
    else:
        count += 1
        continue
else:
    print("So many trials, come back after 5 sec")
    numbers1.countdown(5)

