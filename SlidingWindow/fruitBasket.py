# Dynamic window size problem
def totalFruit(fruits):
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


print(totalFruit([1,2,1]))                  # 3
print(totalFruit([0,1,2,2]))                # 3
print(totalFruit([1,2,3,2,2]))              # 4
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))  # 5

