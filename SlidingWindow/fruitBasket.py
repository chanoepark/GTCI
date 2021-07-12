"""
LC 904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. 
    There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) 
    while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.
"""

# Dynamic window size problem
def totalFruit(fruits):
    # My solution
    (start, maxCount, currCount, basketMap) = (0, 0, 0, {})
    
    for end in range(len(fruits)):
        currFruit = fruits[end]
        
        # Check if fruit is in basket
        if currFruit in basketMap:
            # Increment count of valid fruit
            basketMap[currFruit] += 1
            currCount += 1
        else:
            # Encountered new fruit type
            while len(basketMap) == 2:
                # Adjust the start until one type of fruit is discarded
                prevFruit = fruits[start]
                basketMap[prevFruit] -= 1
                
                if basketMap[prevFruit] == 0:
                    basketMap.pop(prevFruit)
                
                start += 1
                currCount -= 1

            # Store new fruit type
            basketMap[currFruit] = 1
            currCount += 1
        
        if currCount > maxCount:
            # Update max
            maxCount = currCount
    
    return maxCount


def totalFruitImproved(fruits):
    # Most upvoted solution on LeetCode
    (prev1, prev1Count, prev2, currMax, maxCount) = (-1, 0, -1, 0, 0)

    for fruit in fruits:
        if fruit == prev1 or fruit == prev2:
            # Fruit type already in basket
            currMax += 1
        else:
            # Encountered new fruit type
            # Count will now be count of previous fruit plus 1
            currMax = prev1Count + 1
        
        # Update previous fruit count
        if fruit == prev1:
            prev1Count += 1
        else:
            # Update fruit types
            prev1Count = 1
            prev2 = prev1
            prev1 = fruit
        
        if currMax > maxCount:
            # Update max
            maxCount = currMax
        
    return maxCount
        

case1 = [1,2,1]
case2 = [0,1,2,2]
case3 = [1,2,3,2,2]
case4 = [3,3,3,1,2,1,1,2,3,3,4]

print(totalFruit(case1))  # 3
print(totalFruit(case2))  # 3
print(totalFruit(case3))  # 4
print(totalFruit(case4))  # 5

print(totalFruitImproved(case1))  # 3
print(totalFruitImproved(case2))  # 3
print(totalFruitImproved(case3))  # 4
print(totalFruitImproved(case4))  # 5

