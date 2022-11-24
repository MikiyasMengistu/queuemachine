import colors


def display_1():
    products = {"c": "cosmetic", "pe": "perfume", "ph": "pharmacy"}
    print(colors.YELLOW,"Welcome to our drugstore!".center(49))
    for key, val in products.items():
        print(colors.MAGENTA, colors.BOLD, f"\t\tChoose, {key} - for {val} products")