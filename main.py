import os
from writer import *
import platform

platform.system()
def new_show():
    print("Show :", end=" ")
    name = input()
    create_show(name)
    pak()

def print_shows():
    shows = read_shows()

    if not shows:
        print("No shows in playlist!")
        return

    for i in range(len(shows)):
        print("[{}] - {}".format(i, shows[i]["name"]))
    return 1


def show_playlist():
    print_shows()
    pak()


def update():
    if print_shows() is None:
        print("No shows in playlist!")
        pak()
        return

    print("Option :",end=" ")
    num = int(input())
    update_show(num)
    pak()

options = {
    1 : ("New Show", new_show),
    2 : ("Update Show", update),
    3 : ("Show Playlist", show_playlist),
    4 : ("Remove Show", exit),   #WIP
    5 : ("Download Show (WIP)", exit), #WIP
    0 : ("Exit", exit)
}

def clear_screen():
    if platform.system() == 'Windows':
        x = os.system('CLS')
    else:
        x = os.system('clear')


def pak():
    print("Press ENTER to continue")
    x = input()


def menu():
    print("Television Series Manager\n")
    for num in options:
        print("[{}] : {}".format(num, options[num][0]))

    print("Option :", end = " ")


while True:
    clear_screen()
    menu()
    num = int(input())
    options[num][1]()
