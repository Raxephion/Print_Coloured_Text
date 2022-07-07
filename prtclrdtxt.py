# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:18:05 2022

@author: Pierre-Henri Rossouw

60 Apps in 60 Days Challenge - App #10: Print Coloured text

"""


import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is Octagon "+ Fore.YELLOW+ Back.BLUE+"I am your Machine Learning Instructor")
print(Back.CYAN+"Hi My name is Octagon")
print(Fore.RED + Back.GREEN+ "Hi My name is Octagon")