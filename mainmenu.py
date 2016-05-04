import sys,time
import os
# from sportsball import sportsball
#
# # Init Sportsball
# sb = sportsball()


run = True

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.flush()


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')

menu_items = [ 'See all the things',
               'Add Data to DB',
               'Remove Data',
               'Search the DB']

menu_dict = {1:'Things'}

def main_menu():
    clear()
    for i, item in enumerate(menu_items):
        print_slow("{}. {}\n".format(i+1, item))

    user_input = input(">>> ")



main_menu()