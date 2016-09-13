# -*- coding: utf-8 -*-

'''
main routine for orbital

Name: orbital.py

Purpose: Main routine to simulate orbital objects

Author: Tim Cole

History-
Vers Date         By  Description
0.1  03 Sep 2016  THC Initial layout of the Walker Constellation generation 
                      function
                      
Problems/Notes
Num  Date       Resolved  By  Description
001  03 Sep 16  10 Sep 16 THC Initial layout and header
'''

#import os
#import math
#import random
import walker    # lib for Walker constellations

altitude = 1000.0
inclination = 70.0

for numSats in range(1,9):
    print (altitude, inclination, numSats)
    walker.findWalker(altitude, inclination, numSats+1)
    
    
