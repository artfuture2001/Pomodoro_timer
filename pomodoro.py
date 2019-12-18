import time
from os import system, name


def ready_clear():
    # for less code
    print("If ready, press Enter")
    input()
    clear()


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac and linux name is posix
    else:
        _ = system('clear')


def Timer(seconds):
    # simple live timer from youtube tutorial
    while seconds > 0:
        m, s = divmod(seconds, 60)
        time_left = f"{str(m).zfill(2)} : {str(s).zfill(2)}"
        print(time_left + "\r", end="")
        time.sleep(1)
        seconds -= 1
        clear()


def poms_done(poms):
    # for less prints
    print(f"Pomodoros done: {poms}")


total_pomodoros = 0  # pomodoros counter
# minutes * 60 =  seconds
task = 25 * 60
longbreak = 25 * 60
shortbreak = 5 * 60
while True:
    clear()
    poms_done(total_pomodoros)
    starter = input("Start Pomodoro?(Y/N): ")
    clear()
    if starter == "Y":
        total_pomodoros += 1
        print(f"Pomodoro {total_pomodoros}")
        print("*TASK*")
        Timer(task)
        # according to method, after 4th pomodoro, break must be 25 mins
        if total_pomodoros % 4 == 0:
            poms_done(total_pomodoros)
            print("You have deserved long break!)")
            ready_clear()
            poms_done(total_pomodoros)
            print("*LONG BREAK*")
            Timer(longbreak)
            continue
        else:
            poms_done(total_pomodoros)
            print("Time for little break)")
            ready_clear()
            poms_done(total_pomodoros)
            print("*SHORT BREAK*")
            Timer(shortbreak)
            continue
    elif starter == "N":
        poms_done(total_pomodoros)
        print("Bye")
        break
    else:
        print("Try again")
        continue
