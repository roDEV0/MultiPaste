import keyboard
import pyperclip
import configparser
import win32clipboard
import sys

iterationPassthrough = 5
iterationStorage = [""] * 5

defaultKey1 = "ctrl"
defaultKey2 = "alt"

print(r" __  __ _    _ _   _______ _____ _____         _____ _______ ______        _    _")
print(r"|  \/  | |  | | | |__   __|_   _|  __ \ /\    / ____|__   __|  ____|      (_)  / )")
print(r"| \  / | |  | | |    | |    | | | |__) /  \  | (___    | |  | |__           | (_/ ")
print(r"| |\/| | |  | | |    | |    | | |  ___/ /\ \  \___ \   | |  |  __|         _+/  ")
print(r"| |  | | |__| | |____| |   _| |_| |  / ____ \ ____) |  | |  | |____       //|\\")
print(r"|_|  |_|\____/|______|_|  |_____|_| /_/    \_\_____/   |_|  |______|     // | )")
print(r"                                                                        (/  |/")
print("Welcome to MultiPaste")
print("You are currently running version 0.5")
print("Type 'help' and press enter for a basic list of commands")
print("Created by Gianmichael Romano")


def copy(iterationPassthrough):
    clipboard = win32clipboard
    clipboard.OpenClipboard()
    try:
        iterationStorage[iterationPassthrough - 1] = clipboard.GetClipboardData()
        print(f"Copied {clipboard.GetClipboardData()} to iteration {iterationPassthrough}")
    finally:
        clipboard.CloseClipboard()

def paste(iterationPassthrough):
    keyboard.write(iterationStorage[iterationPassthrough - 1])

for i in range(1, 6):
    keyboard.add_hotkey(defaultKey1 + ' + ' + defaultKey2 + ' + c + ' + str(i), lambda i=i: copy(i))
    keyboard.add_hotkey(defaultKey1 + ' + ' + defaultKey2 + ' + v + ' + str(i), lambda i=i: paste(i))

def cmdHandler(inputcmd):
    if inputcmd == "show":
        displayLines()
    elif inputcmd.startswith("clean"):
        if len(inputcmd.split()) == 1:
            clean()
            print("All iterations cleared")
        else:
            try:
                iteration = int(inputcmd.split()[1])
                clean(iteration)
                print(f"Iteration {iteration} cleared")
            except ValueError:
                print("Invalid input for clean command")
    elif inputcmd == "help":
        help()
    elif inputcmd == "exit":
        sys.exit()
    else:
        print("Not a valid command")

def displayLines():
    print("Iteration Storage:")
    for i in range(len(iterationStorage)):
        print(str(i + 1) + ": " + iterationStorage[i])

def clean(iteration=None):
    if iteration is None:
        for i in range(len(iterationStorage)):
            iterationStorage[i] = ""
    elif 1 <= iteration <= len(iterationStorage):
        iterationStorage[iteration - 1] = ""
    else:
        print("Invalid iteration number")

def help():
    print("SHOW <optional: Number> - Shows the iteration stored to the specified number. If left blank, shows all iterations.")
    print("CLEAN <optional: Number> - Empties the iteration stored to the specified number. If left blank, will clear all iterations.")
    print("EXIT - Exits Multipaste. Does NOT save your current iterations.")

while True:
    cmd = input("")
    cmdHandler(cmd)
