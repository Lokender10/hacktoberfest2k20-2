import math
import os
import random
import re
import sys



def receivedText(S):
    s=list(S)
    a=[]
    b=[]
    e=[]
    t=[]
    p=0
    i=0
    n=0
    a.append(e)
    Num="1234567890"
    for i in range(len(s)):
        if(s[i]=='<'):
            e=[]
            a.append(e)
            p=len(a)-1
        elif(s[i]=='>'):
            e=[]
            a.insert(0,e)
            p=0
        elif(s[i]=='#' and n==0):
            n=1
        elif(s[i]=='#' and n==1):
            n=0
        elif(s[i]=='*'):
            j=p
            while(j<len(a)):
                if(not a[j]):
                    print('abc')
                else:
                    del(a[j][-1])
                    break
                j+=1
                
                
        if(s[i]!='<' and s[i]!='>' and s[i]!='#' and s[i]!='*'):
            if (s[i] in Num and n==1):
                print("abc")           
            else:    
                a[p].append(s[i])
    
    ans=""
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a[i])):
            ans+=str(a[i][j])  
    return(ans)      

        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    result = receivedText(S)

    fptr.write(result + '\n')

    fptr.close()
