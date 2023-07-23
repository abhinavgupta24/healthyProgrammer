# a healthy programmer
"""we have to make functions for eye , exercise , and drink water"""
import time

from datetime import datetime


def eye():
    from pygame import mixer
    mixer.init()
    mixer.music.load("ultrainstinct.mp3")
    mixer.music.play()


def exercise():
    from pygame import mixer
    mixer.init()
    mixer.music.load("ultrainstinct.mp3")
    mixer.music.play()


def water():
    from pygame import mixer
    mixer.init()
    mixer.music.load("ultrainstinct.mp3")
    mixer.music.play()


def getdate():
    import datetime
    return datetime.datetime.now()


if _name_ == "__main__":
    log = 20
    inp = input("enter your name : ")
    while log > 1:
        time.sleep(5)
        eye()
        if inp4 == "ey done":
            from pygame import mixer

            mixer.init()
            mixer.music.load("ultrainstinct.mp3")
            mixer.music.stop()
            f = open(f"{inp2}", "w")
            f.write(f"{inp} has done the eye exercise at {getdate()}")
            f.close()
            log = log - 1
        else:
            print(" enter a valid input! after 5 seconds. ")
        time.sleep(5)
        exercise()
        inp5 = input("time to do physical exercise , enter 'ex done' to stop the alarm : ")
        if inp5 == "ex done":
            from pygame import mixer

            mixer.init()
            mixer.music.load("ultrainstinct.mp3")
            mixer.music.stop()
            f = open(f"{inp1}", "w")
            f.write(f"{inp} has done physical exercise at {getdate()}")
            f.close()
            log = log - 1
        else:
            print(" enter a valid input! after 5 seconds. ")
        time.sleep(5)
        exercise()
        inp6 = input("time to drink water , enter 'dw done' to stop the alarm : ")
        if inp6 == "dw done":
            from pygame import mixer

            mixer.init()
            mixer.music.load("ultrainstinct.mp3")
            mixer.music.stop()
            f = open(f"{inp3}", "w")
            f.write(f"{inp} has dranked water at {getdate()}")
            f.close()
            log = log - 1
        else:
            print(" enter a valid input! after 5 seconds. ")  # a healthy programmer
