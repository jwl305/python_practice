#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:59:48 2021

@author: lee7222
"""
import string
file = open("input.txt",'r')

def solve(s):
    L=s.split()
    new=[]
    j1=" ".join(map(str.capitalize,s.split(" ")))
    print(j1)
        
    
if __name__=="__main__":
    name=file.readline()
    solve(name)
