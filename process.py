from display import display_1
from suplier import suplier1
from queue import queue1
from dictionaries import queue_dict


def process1():
    areas = "."
    while areas != "e":
        display_1()
        areas = input("enter 'e' to exit.\nWhich place you want to visit?  ")
        if areas in queue_dict:
            if len(queue_dict[areas]) == 0:
                suplier1(areas)
                queue1(areas)
                del queue_dict[areas][0]
            else:
                queue1(areas)
                del queue_dict[areas][0]

