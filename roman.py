#Hunter Long
#mia014
#CS-3723-01T
#Assignment 7
#August 7th, 2021

import sys

def roman( y ):

   #error checking: make sure value is an int and in range 
   try:
      x = int( y )
   except ValueError:
      return "Error"

   if x <= 0 or x > 3999:
      return "Error"

   #create lists of reference values to be used in translation loop to form the romNum string
   ones = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]
   tens = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
   hundreds = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
   thousands = [ "", "M", "MM", "MMM" ] 
   romVals = [ thousands, hundreds, tens, ones ]

   #initialize variables needed for the translation loop 
   romNum = ""
   divisor = 1000

   #translation loop: 
      #1. find value of current decimal place value
      #2. append appropriate roman numeral to return string 
      #3. move to the next decimal place value down 
   for i in range(0,4):
      value = x // divisor
      romNum = romNum + romVals[i][int(value)]
      x = x % divisor
      divisor = divisor / 10

   return romNum

#short script to iterate through command line arguements, pass them to roman, and print the results
for i in sys.argv[1:]:
   result = roman( i )
   print( str( i ) + " is " + result ) 

