#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""

   def makeChange(coins, total):
        """
	   This function will take a list of coins and use
           that to calculate how much change the total will require
        """
	if total <= 0:
	   return 0

        coins.sort(reverse=True)  # Sort coins in descending order
        counter = 0

        for coin in coins:
           while total >= coin:
               counter += 1
               total -= coin

        return counter if total == 0 else -1
