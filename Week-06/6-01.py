Write a python program to count all letters, digits, and special symbols respectively from a given string



Input	                          Result

rec@123                         3

                                3

                                1






Coding:

a=input()

c,d,s=0,0,0

for i in range(len(a)):

    if(a[i].isalpha()):

        c+=1

    elif(a[i].isdigit()):

        d+=1

    else:

        s+=1

print(c,d,s,sep="\n")
