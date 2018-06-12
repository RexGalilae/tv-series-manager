import os
from writer import *
import platform
import json

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

# Remove Show
def remove_show():
    print_shows()
    print("[D] - Delete All")
    print("Option :", end = " ")
    opt = input()
    if not os.path.exists(DATAFILE):
        print("There are no shows in your playlist.")
    with open(DATAFILE, "r") as dfile:
        shows = json.load(dfile)
    if opt == 'D':
         print("Confirm (Delete All) [Y/N]:"),
         conf = input()
         if conf == 'Y' or conf == 'y':
             shows = []
    else:
        del shows[int(opt)]
    with open(DATAFILE, "w") as dfile:
        shows = json.dump(shows, dfile)
    print("Show(s) successfully deleted!")
    pak()

def exit_program():
    print("Thank You!")
    pak()
    clear_screen()
    exit()

def wip():
    print("Sorry! This feature is unavailable right now. Stay updated!")
    pak()

options = {
    1 : ("New Show", new_show),
    2 : ("Update Show", update),
    3 : ("Show Playlist", show_playlist),
    4 : ("Remove Show", remove_show),   #WIP
    5 : ("Download Show (WIP)", wip), #WIP
    0 : ("Exit", exit_program)
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
