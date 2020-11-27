from Type import *

if __name__ == "__main__":
    print(r"______     _        _   _ _   _ _     ")
    print(r"| ___ \   | |      | | | | | (_) |    ")
    print(r"| |_/ /__ | | _____| | | | |_ _| |___ ")
    print(r"|  __/ _ \| |/ / _ \ | | | __| | / __|")
    print(r"| | | (_) |   <  __/ |_| | |_| | \__ \\")
    print(r"\_|  \___/|_|\_\___|\___/ \__|_|_|___/")
    print("                   version 0.1        ")
    print("======================================")

    i = input("Type of pokemon: ")
    if instance := globals().get(i, None):
        instance = instance()
        print(instance)
    else:
        print("No such type was found. Did you mispelled it?")
    