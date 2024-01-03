import time


print("$# Countdown Generator $#")


def countdown(t):
 
    while t :
        mins , sec =  divmod(t , 60)
        timer = "{:02d}:{:02d}".format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
         


    print("Timer done")


t =  int(input("Please enter the amout of secondes: "))

countdown(t)