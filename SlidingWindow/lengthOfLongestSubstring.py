"""
LC 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

# Dynamic window size problem
def lengthOfLongestSubstring(s: str) -> int:
    # Check if string is empty
    if not s:
        return 0
    
    maxCount = 0
    currCount = 0
    start = 0
    chars = []
    
    for end in range(len(s)):
        curr = s[end]
        
        # Check for repeating character
        while curr in chars:
            # Update left pointer until current character is removed
            chars.remove(s[start])
            start += 1
            currCount -= 1
        
        # Process current substring
        chars.append(curr)
        currCount += 1
        
        # Update maxCount
        if currCount > maxCount:
            maxCount = currCount
    
    return maxCount

case1 = "abcabcbb"
case2 = "bbbbb"
case3 = "pwwkew"
case4 = ""

print(lengthOfLongestSubstring(case1)) # 3
print(lengthOfLongestSubstring(case2)) # 1
print(lengthOfLongestSubstring(case3)) # 3
print(lengthOfLongestSubstring(case4)) # 0

