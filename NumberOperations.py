import sys
import itertools
# import numpy as np
# import pandas as pd
# from sklearn import ...

 

def muts(Lst,size):
    return list(itertools.permutations(Lst,size))

def ops(lst1,lst2):
    for x in lst1:
        for i in lst2:
            op1=i[0]
            op2=i[1]
            op3=i[2]
            op4=i[3]
        
            str1=str(x[0])+op1+str(x[1])
            str2=str(str1)+op2+str(x[2])
            str3=str(str2)+op3+str(x[3])
            str4=str(str3)+op4+str(x[4])
            exp=eval(str4)

            if(exp==42):
                return True
    return False

Numb=[int(i) for i in input().split(" ")]

NumPermuts=muts(Numb,5)

Operators=['+','-','*','+','-','*']

OpPermutations=muts(Operators,4)

Result=ops(NumPermuts,OpPermutations)

if(Result==True):
    print("YES")
else:
    print("NO")
