
vowels=['A','E','I','O','U']
import string

    
def minion_game(s):
    Vowels="AEIOU"
    K=0
    S=0
    for i in range(len(s)):
        if s[i] in Vowels:
            K+= len(s)-i
        else:
            S+= len(s)-i
    if K>S:
        print("Kevin",K)
    elif K<S:
        print("Stuart",S)
    else:
        print("Draw")
    

file=open("input.txt",'r')

if __name__=="__main__":
    s=file.readline()
    minion_game(s)
