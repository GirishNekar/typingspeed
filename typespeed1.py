from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error        
            

        

    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test = ["girish is typing","If there's one thing a rough patch. We even curatenced the same things as you can go a long way."]

test1 = r.choice(test)
print("  *****  Typing Speed  *****  ")
print(test1)
print()
print()
time_1 = time()
print("* Enter The given Paragraph that have same number of words as given in the above paragraph *:")
print("NOTE:Space is also considered as word")
print("Please enter your paragraph below")
testinput = input()
time_2 = time()

print("Speed: ", speed_time(time_1, time_2, testinput), " words/sec")
print("Error: ", mistake(test1, testinput))
