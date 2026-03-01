# FILE NAME - coin_toss.py

# NAME:Patrick Babb 
# DATE:3/1/2026 
# BRIEF DESCRIPTION: creating a coin toss program  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
import random
def main():
    coin_toss()
def coin_toss():
    coin_flip = random.randint(0,100)
    print('===== Coin Flipper =====')
    if (coin_flip > 50):
        print('Tails')
    else:
        print('Heads')
main()





########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Putting in the definition and then assigning it to an if and else function was somewhat challenging as well as getting
used to the syntax.






'''
