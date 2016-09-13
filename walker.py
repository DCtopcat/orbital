# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 09:43:35 2016

@author: Tim
"""
'''

Name: walker.py

Purpose: Walker Constellation implementation code

Author: Tim Cole

History-
Vers Date         By  Description
0.1  03 Sep 2016  THC Initial layout of the Walker Constellation generation 
                      function
                      
Problems/Notes
Num  Date       Resolved  By  Description
001  03 Sep 16  10 Sep 16 THC Initial layout and header
'''

import random

def findWalker(alt, inc, n):
    ''' 
    Function: find the potential walker constellations for n satellites
    input: n number of satellites
    output: list of number of potential rings
    '''
    # loop through the numbers from 0 to n/2 to find factors of n
    max = int((n/2) + 1)
    if (n == 2):
        max = 2
    for ind in range(1, max):
        if (n%ind == 0):
            print ("Potential number of walker rings identified: " + str(ind))
            for F in range(0,n+1):
                print ("The Walker parameters are " + str(n) + "," + str(ind) + "," + str(F))
                satList = assignWalkerParams(alt, inc, n, ind, F)
                #print ("satList is " + str(satList))
                cover = assessWalkerCoverage(satList)
                print ("Coverage is " + str(cover) + "\n")
    return
    
def assessWalkerCoverage(w):
    '''
    Function: Assess the coverage provided by the specified Walker Constellation
    Input: List containing the constellation to be assessed
    Output: Coverage number
    '''
    coverage = 10000.0 * random.random()
    return coverage
    
def assignWalkerParams(alt,inc,T,R,F):
    '''
    Function: Create orbital parameters based on the walker numbers
    Input: Walker parameters
    Output: List containing the constellation with orbital params
    '''
    # Calculate the orbital position at epoch for the constellation
    satList = []
    ringNum = 0
    rightAscensionOffset = 360. / R
    # Change in true anomaly between satellites in adjacent rings (planes)
    ringOffset = 360. * (F / T)
    numSatInRing = T/R
    # Initialize satellite ring variables
    numInRing = 0
    ringNum = 0
    #print (str(numSatInRing))
    #print ("Right Ascension Offset " + str(rightAscensionOffset))
    #print ("Ring Offset " + str(ringOffset))
    for sat in range(1,T+1):
        #print ("Computing parameters for satellite number " + str(sat) + "\n")
        satParams = []
        numInRing = numInRing + 1
        if ((sat - 1)%numSatInRing == 0):
            ringNum = ringNum + 1
            numInRing = 1
        #print ("Satellite " + str(sat) + " Ring Params " + str(ringNum) + ", " + str(numInRing))
        satRightAscension = (ringNum - 1) * rightAscensionOffset
        satAnomaly = ((ringNum + numInRing) * ringOffset)%360.
        #print ("Satellite " + str(sat) + " " + str(ringNum) + " " + str(numInRing) + " has an anomaly of " + str(satAnomaly))
        #Store the satellite data
        satParams.append(sat)
        satParams.append(ringNum)
        satParams.append(numInRing)
        satParams.append(alt)
        satParams.append(inc)
        satParams.append(satRightAscension)
        satParams.append(satAnomaly)
        satList.append(satParams)
    return satList
    
    