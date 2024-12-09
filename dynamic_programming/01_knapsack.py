"""
Given N items where each item has some weight and profit associated with it and
also given a bag with capacity W, [i.e., the bag can hold at most W weight in
it].

The task is to put the items into the bag such that the sum of profits
associated with them is the maximum possible.

Note: The constraint here is we can either put an item completely into the bag
or cannot put it at all [It is not possible to put a part of an item into the
bag].

Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If
we select the item with weight 4, the possible profit is 1. And if we select
the item with weight 1, the possible profit is 3. So the maximum possible
profit is 3. Note that we cannot put both the items with weight 4 and 1
together as the capacity of the bag is 4.


Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0
"""

from pprint import pprint


N = 3  # number of items
# W = 4  # max carrying weight of knapsack
profit = [1, 2, 3]  # profit of item at index
weight = [4, 5, 1]  # weight of item at index


# Using dynamic programming
def dp_solution(capacity: int, profit: list[int], weight: list[int]):
    N = len(profit)
    # create table for dp, rows are onjects and cols are different weights
    dp = [[0] * (capacity + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w - 1],
                    (dp[i - 1][w - weight[i - 1]] + profit[i - 1]),
                )
            else:
                dp[i][w] = dp[i - 1][w]

    current = dp[-1][-1]  # greatest profit in last row last col
    result = [0] * N  # binary array to show whether item is included
    for i in range(N, 0, -1):
        # intuition: if current max profit not found in previous row, current
        # item is included since it caused an increase in profit
        if current not in dp[i - 1]:
            result[i - 1] = 1  # set item to included
            current -= profit[i - 1]  # deduct profit of included item

    pprint(dp)
    return result


def main():
    print("Problem 1")
    print(dp_solution(4, [1, 2, 3], [4, 5, 1]))
    print("Problem 2")
    print(dp_solution(8, [1, 2, 5, 6], [2, 3, 4, 5]))


if __name__ == "__main__":
    main()
