import math
import time


#ik ik my var nameing is dog shit, no no plz feel free to tell me all about how im over using brackets and how you would have done it soooo much better


i = 1
j = 1
l = 1
leg = []

#main loop
while True:
    sinx = round((((round(10*(math.sin(l))))+10)*3)) + 200
    sinw = round((((round(10*(math.sin(j))))+10)*3)) + 200
    sinn = round((((round(10*(math.sin(i))))+10)*3)) + 200
    #this is used to generate a number (sinn) that gose up and down from 0 - 20 in the sin wave mannor
    #it finds the sin of "i", * 10 and adds +10 (to avoid neg numbers) rounds, /2 and rounds again
     
    time.sleep(0.03)    #slows the program down          
    i += 0.1
    j += 0.2
    l += 0.15
    print("####".center(int(sinn)))
    print("_-_-".center(int(sinw)))
    print("*/*/".center(int(sinx)))
