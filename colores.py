def colors(texto):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    if color.lower() == "rojo":
        print(f"{RED} {color}")
    elif color.lower() == "verde":
        print(f"{GREEN} {color}")
    elif color.lower() == "amarillo":
        print(f"{YELLOW} {color}")
    elif color.lower() == "azul":
        print(f"{BLUE} {color}")
if __name__ == '__main__':
    colors("")
