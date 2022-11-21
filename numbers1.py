import colors
import time
queue_dict = {"c": [], "pe": [], "ph": []}
customers = ['346402183', '341343390']


def nums():
    for i in range(1, 100):
        yield i


def suplier(section):
    for i in nums():
        queue_dict[section].append(i)


def display():
    products = {"c": "cosmetic", "pe": "perfume", "ph": "pharmacy"}
    print(colors.YELLOW,"Welcome to our drugstore!".center(49,))
    for key, val in products.items():
        print(colors.MAGENTA, colors.BOLD, f"\t\tChoose, {key} - for {val} products")


def process():
    areas = "."
    while areas != "e":
        display()
        areas = input("enter 'e' to exit.\nWhich place you want to visit?  ")
        if areas in queue_dict:
            if len(queue_dict[areas]) == 0:
                suplier(areas)
                queue(areas)
                del queue_dict[areas][0]
            else:
                queue(areas)
                del queue_dict[areas][0]

def queue(show):
    a = "Your number is"
    b = "Please wait and someone will assist you shortly."
    print(colors.GREEN,f"{a}\n{show} - {queue_dict[show][0]}\n{b}")


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")






































