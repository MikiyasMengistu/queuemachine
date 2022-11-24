
import colors
from dictionaries import queue_dict


def queue1(show):
    a = "Your number is"
    b = "Please wait and someone will assist you shortly."
    print(colors.GREEN,f"{a}\n{show} - {queue_dict[show][0]}\n{b}")