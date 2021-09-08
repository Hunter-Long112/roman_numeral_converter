#Hunter Long
#CS-3723
#Assignment 7
#August 7th, 2021

#import the functions from roman.py and namor.py
from roman import *
from namor import *

#test loop:
   #1. Pass int to roman to have it converted to a roman numeral string 
   #2. Pass the string returned by roman to namor to have it converted back to an int
   #3. make sure the int returned by namor is the same as the original int, if not print error message and 
   #   add one to the number of errors
numErrors = 0
for k in range(0, 4001):
   romanTester = roman( k )
   namorTester = namor( romanTester )
   if namorTester != k:
      print( "Converted " + str( k ) + " to " + romanTester + " back to " + str( namorTester ) + ", which is wrong." )
      numErrors += 1

#print out testing "report"
print( "Checked values from 0 to 4000. Errors = " + str( numErrors ) + "." )

