from number_generator import number_generator1
from dictionaries import queue_dict


def suplier1(section):
    for i in number_generator1():
        queue_dict[section].append(i)