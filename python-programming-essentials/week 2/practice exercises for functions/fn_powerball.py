"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    num1 = random.randrange(1, 60)
    num2 = random.randrange(1, 60)
    num3 = random.randrange(1, 60)
    num4 = random.randrange(1, 60)
    num5 = random.randrange(1, 60)
    num6 = random.randrange(1, 36)
    print("Today's numbers are " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", and " + str(num5) + ". ", end = "")
    print("The Powerball number is " + str(num6) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
