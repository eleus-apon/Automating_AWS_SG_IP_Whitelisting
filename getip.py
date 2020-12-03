# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:26:33 2020

@author: MT_Eleus
"""

import urllib.request

public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

with open('foundip.txt', 'w') as f:
    f.write(public_ip)
