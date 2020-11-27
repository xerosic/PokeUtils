from Type import *

if __name__ == "__main__":
    i = input("Type of pokemon: ")
    if instance := globals().get(i, None):
        instance = instance()
        print("\n" + instance)
    else:
        print("No such type was found. Did you mispelled it?")
    