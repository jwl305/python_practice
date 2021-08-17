#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:47:03 2021

@author: lee7222
"""
import string
file = open("input.txt",'r')


def pyramid(inputlist,size):
    new=[]
    for each in range(size):
        snip="-".join(inputlist[each:size])
        new.append(snip[::-1]+snip[1:])
    return new

def print_rangoli(n):
    size=4*n-3
    letters=[]
    alphabet=string.ascii_lowercase
    new=pyramid(alphabet,n)
    print(new)
    for each in range(n):
        print(new[n-each-1].center(size,"-"))    
    for each in range(n-1):
       print(new[each+1].center(size,"-"))        
if __name__ == '__main__':
    
    n = int(file.readline())
    print_rangoli(n)
