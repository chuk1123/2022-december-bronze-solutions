"""
USACO December 2022 Bronze - Problem 1: Cow College
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1251

Problem Summary:
Determine the optimal tuition price for Farmer John's cow college.
Given N cows with their maximum willingness to pay, find the price that
maximizes revenue (price × number_of_enrollments).

Algorithm: Greedy with Sorting
- Sort willingness-to-pay values in descending order
- For each price point, calculate revenue = price × students_willing_to_pay
- Track maximum revenue and corresponding price

Time Complexity: O(n log n)
Space Complexity: O(n)

Author: Kevin Chu (chuk1123)
"""

def solve():
    # Read number of cows
    N = int(input())

    # Read willingness-to-pay values for each cow
    A = list(map(int, input().split()))

    # Sort in descending order - highest willingness first
    # This allows us to efficiently calculate how many cows would enroll at each price
    sorted_prices = sorted(A, reverse=True)

    # Track maximum profit and optimal price
    max_profit = 0
    optimal_price = 0

    # Try each unique price point
    for i in range(len(sorted_prices)):
        current_price = sorted_prices[i]

        # Calculate revenue if we set tuition to current_price
        # All cows from index 0 to i are willing to pay this much
        # So (i + 1) students would enroll
        profit = current_price * (i + 1)

        # Update if this is the best revenue we've found
        # Using >= ensures we take the smallest price if there's a tie
        if profit >= max_profit:
            max_profit = profit
            optimal_price = current_price

    # Output: maximum revenue and corresponding tuition price
    print(max_profit, optimal_price)

solve()
