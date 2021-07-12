"""
LC 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

# Dynamic window size problem
def lengthOfLongestSubstring(s: str) -> int:
    # My solution
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


def lengthOfLongestSubstringSimple(s: str) -> int:
    # Simpler solution from LC discussion post
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            output = max(output,r-l+1)
        else:
            """
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            """
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    
    return output


case1 = "abcabcbb"
case2 = "bbbbb"
case3 = "pwwkew"
case4 = ""

print(lengthOfLongestSubstring(case1)) # 3
print(lengthOfLongestSubstring(case2)) # 1
print(lengthOfLongestSubstring(case3)) # 3
print(lengthOfLongestSubstring(case4)) # 0

