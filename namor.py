#Hunter Long
#mia014
#CS-3723-01T
#Assignment 7
#August 7th, 2021

import sys

def namor( tempRomNum ):

   #make sure string is all uppercase
   romNum = tempRomNum.upper()

   #error checking: make sure string only uses valid roman numeral symbols 
   validSymbols = [ "I", "V", "X", "L", "C", "D", "M" ]
   for j in romNum:
      if j not in validSymbols:
         return 0

   #error checking: make sure the string is a valid roman numeral by making sure there isn't 4 of the same 
   #symbols in a row (this will also make sure it is less than 4000)
   numInRow = 0
   for j in range(1, len(romNum)):
      if romNum[j] == romNum[j-1]:
         numInRow += 1
      if romNum[j] != romNum[j-1]:
         numInRow = 0
      if numInRow == 3:
         return 0

   #create lists of reference values to be used in translation loops
   ones = [ ["IX", 9], ["VIII", 8], ["VII", 7], ["VI", 6], ["V", 5], ["IV", 4], ["III", 3], ["II", 2], ["I", 1] ]
   tens = [ ["XC", 90], ["LXXX", 80], ["LXX", 70], ["LX", 60], ["L", 50], ["XL", 40], ["XXX", 30], ["XX", 20], ["X", 10] ] 
   hundreds = [ ["CM", 900], ["DCCC", 800], ["DCC", 700], ["DC", 600], ["D", 500], ["CD", 400], ["CCC", 300], ["CC", 200], ["C", 100] ]
   thousands =[ ["MMM", 3000], ["MM", 2000], ["M", 1000] ]

   #initialize variables needed for translation loops
   num = 0
   nextStart = 0

   #translation loops:
      #1. find the value of the current decimal place value in string 
      #2. add value to our decimal number 
      #3. move "cursor position" past current decimal place value 
      #4. repeat for thousands, hundreds, tens, and ones place 
   for i in range(0, 3):
      if romNum.startswith( thousands[i][0] ):
         num += thousands[i][1]
         nextStart = len( thousands[i][0] )
         break

   for i in range(0, 9):
      if romNum.startswith( hundreds[i][0], nextStart ):
         num += hundreds[i][1]
         nextStart += len( hundreds[i][0] )
         break

   for i in range(0, 9):
      if romNum.startswith( tens[i][0], nextStart ):
         num += tens[i][1]
         nextStart += len( tens[i][0] )
         break

   for i in range(0, 9):
      if romNum.startswith( ones[i][0], nextStart ):
         num += ones[i][1]
         nextStart += len( ones[i][0] )
         break

   if nextStart != len( romNum ):
      return 0

   return num

#short script to iterate through command line arguements, pass them to namor, and print the results
for i in sys.argv[1:]:
   result = namor( i )
   print( i + " is " + str( result ) ) 

