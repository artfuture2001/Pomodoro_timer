import time
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def ready():
    print("If ready, press Enter")
    input()


def Timer(seconds):
    while seconds > 0:
        m, s = divmod(seconds, 60)
        time_left = f"{str(m).zfill(2)} : {str(s).zfill(2)}"
        print(time_left + "\r", end="")
        time.sleep(1)
        seconds -= 1


total_pomodoros = 0
task = 25
longbreak = 25
shortbreak = 5
while True:
    clear()
    print(f"Pomodoros done: {total_pomodoros}")
    starter = input("Start Pomodoro?(Y/N): ")
    clear()
    if starter == "Y":
        total_pomodoros += 1
        print(f"Pomodoro {total_pomodoros}")
        print("*TASK*")
        Timer(task)
        clear()
        if total_pomodoros % 4 == 0:
            print(f"Pomodoros done: {total_pomodoros}" +
                  "\nYou have deserved long break!)")
            ready()
            clear()
            print(f"Pomodoros done: {total_pomodoros}")
            print("*LONG BREAK*")
            Timer(longbreak)
            clear()
            continue
        else:
            print(f"Pomodoros done: {total_pomodoros}" +
                  "\nTime for little break)")
            ready()
            clear()
            print(f"Pomodoros done: {total_pomodoros}")
            print("*SHORT BREAK*")
            Timer(shortbreak)
            clear()
            continue
    elif starter == "N":
        print(f"Pomodoros done: {total_pomodoros}")
        print("Bye")
        break
    else:
        print("Try again")
        continue
