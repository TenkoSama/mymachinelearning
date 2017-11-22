
from numpy import *


def myLevenstein(str1,str2):
    if (str1==str2):
        return int(0)
    else:
        i = len(str1)
        j = len(str2)
        if (i==0) :
            return j   
        elif (j==0):
            return i
        else:
            cost = int(0) if str1[-1]==str2[-1] else int(1)
            return min(myLevenstein(str1[:-1],str2[:-1]),\
        myLevenstein(str1[:-1],str2),myLevenstein(str1,str2[:-1]))\
        +cost
    

