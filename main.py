from operator import index
from re import L
from data import Purchase_dept_Marianne_Emond, Refund_Marianne_Emond
from logic import KiksBank, clearConsole
import time
import sys
import pickle
import os


def menu():
    print("\n\n")
    print("//   /$$   /$$ /$$ /$$       /$$                    /$$$$$$$                      /$$      ")
    print("//  | $$  /$$/|__/| $$      | $/                   | $$__  $$                    | $$      ")
    print("//  | $$ /$$/  /$$| $$   /$$|_//$$$$$$$            | $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$")
    print("//  | $$$$$/  | $$| $$  /$$/  /$$_____/            | $$$$$$$  |____  $$| $$__  $$| $$  /$$/")
    print("//  | $$  $$  | $$| $$$$$$/  |  $$$$$$             | $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ ")
    print("//  | $$\  $$ | $$| $$_  $$   \____  $$            | $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ ")
    print("//  | $$ \  $$| $$| $$ \  $$  /$$$$$$$/            | $$$$$$$/|  $$$$$$$| $$  | $$| $$ \  $$")
    print("//  |__/  \__/|__/|__/  \__/ |_______/             |_______/  \_______/|__/  |__/|__/  \__/")
    print("                                                                                             [developped by: Karim Khiari]\n\n\n\n\n")


def choice():
    print("[ 1 ] . . .  Show a detailed chart of my previous purshases and calculate my Dept to Kik's Bank ©\n\n")
    print("[ 2 ] . . .  Show a detailed chart of my previous refunds and calculate what I Paid to Kiks's Bank ©\n\n")
    print("[ 3 ] . . .  Adding a Dept to my current Dept balance at Kik's Bank ©\n\n")
    print("[ 4 ] . . .  Adding a Refund to my current Refund balance at Kiks's Bank ©\n\n")
    print("[ 5 ] . . .  Deleting a Dept to my current Dept balance at Kik's Bank ©\n\n")
    print("[ 6 ] . . .  Deleting a Refund to my current Refund balance at Kiks's Bank ©\n\n")
    print("[ 7 ] . . .  Show my current balance between my depts and my refunds to see how much money I owe to Kik's Bank ©\n\n\n")
    print("{ 0 } . . .  SAVE & EXIT Kik's Bank software © . . .\n\n\n\n")
    action = input("Please Enter the number corresponding to the action desired ~~~>  ")
    clearConsole()
    return action


def intro():
    time.sleep(1)
    print("                                     [ K software ]  ==>  At Kiks foundation,")
    print("                                                          we value stability,")
    print("                                                          and finance health.\n\n\n\n\n")
    time.sleep(2.5)
    print("                                     This software is designed to keep track")
    print("                                     of your depts using visual graphs,")
    print("                                     and a built-in calculator to automate")
    print("                                     mathematical processing in order to avoid")
    print("                                     human mistakes while counting your balance.\n\n\n\n\n\n\n")
    time.sleep(3)
    start = input("                                             [PRESS ENTER TO CONTINUE]")
    clearConsole()
    return start


def initialization():
    # Checks if a save folder exist, if not creates one and initialize a dept and a refund dictionnary
    dir_list = os.listdir()
    last_index = len(dir_list) - 1
    check = True
    absolute_path = os.getcwd()
    for i, dir in enumerate(dir_list):
        if dir == "saves":
            check = False
            os.chdir(dir)
            fich = os.listdir()[-1]
            f = open(fich, 'rb')
            u = pickle.Unpickler(f)
            saved_INVOICE = u.load()
            os.chdir(absolute_path)
            return saved_INVOICE
        if check and i == last_index:
            os.mkdir("saves")
            Marianne_Emond = [Purchase_dept_Marianne_Emond, Refund_Marianne_Emond]
            #initialize = [{}, {}]
            return Marianne_Emond


def exit_software():
    print("  ______    ______    ______   _______         _______   __      __  ________ ")
    print(" /      \  /      \  /      \ /       \       /       \ /  \    /  |/        |")
    print("/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$$  |      $$$$$$$  |$$  \  /$$/ $$$$$$$$/ ")
    print("$$ | _$$/ $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |__$$ | $$  \/$$/  $$ |__    ")
    print("$$ |/    |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$    $$<   $$  $$/   $$    |   ")
    print("$$ |$$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$$$$$$  |   $$$$/    $$$$$/    ")
    print("$$ \__$$ |$$ \__$$ |$$ \__$$ |$$ |__$$ |      $$ |__$$ |    $$ |    $$ |_____ ")
    print("$$    $$/ $$    $$/ $$    $$/ $$    $$/       $$    $$/     $$ |    $$       |")
    print(" $$$$$$/   $$$$$$/   $$$$$$/  $$$$$$$/        $$$$$$$/      $$/     $$$$$$$$/ ")
    sys.exit()



if __name__ == "__main__":
    user = initialization()
    INVOICE = KiksBank(user[0], user[1])
    show_intro = True

    while True:
        if show_intro:
            menu()
            switcher = intro()
            if switcher == '':
                show_intro = False
        menu()
        action = choice()
        if action == '1':
            print(INVOICE.show_dept())
        if action == '2':
            print(INVOICE.show_refund())
        if action == '3':
            print(INVOICE.add_dept())
        if action == '4':
            print(INVOICE.add_refund())
        if action == '5':
            print(INVOICE.delete_dept())
        if action == '6':
            print(INVOICE.delete_refund())
        if action == '7':
            print(INVOICE.show_new_balance())
        if action == '0':
            absolute_path = os.getcwd()
            os.chdir("saves")
            dir_list = os.listdir()
            if dir_list == []:
                f = open('0.pkl', 'wb')
                p = pickle.Pickler(f)
                p.dump(INVOICE.get_dept_refund())
                f.close()
            else:
                dir_num = int(dir_list[-1][:-4]) + 1
                dir_name = f"{dir_num}.pkl"
                f = open(dir_name, 'wb')
                p = pickle.Pickler(f)
                p.dump(INVOICE.get_dept_refund())
                f.close()
            os.chdir(absolute_path)
            exit_software()
        input("                                             [PRESS ENTER TO CONTINUE]")
