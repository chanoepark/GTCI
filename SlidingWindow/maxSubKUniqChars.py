# Dynamic window size problem
def longest_substring_with_k_distinct(str1, k):
    (start, chars, currLen, maxLen) = (0, {}, 0, 0)

    # Return immediately if k equals 0
    if k == 0:
        return 0

    for end in range(len(str1)):
        curr = str1[end]

        if curr in chars:
            # Valid char repeat
            currLen += 1
            chars[curr] += 1
        elif len(chars) < k:
            # Valid new char
            chars[curr] = 1
            currLen += 1
        else:
            # Exceeded k
            # Update start of window until uniq chars decreases by 1
            while len(chars) == k:
                startChar = str1[start]
                if chars[startChar] > 1:
                    chars[startChar] -= 1
                else:
                    chars.pop(startChar)
                start += 1
                currLen -= 1
            
            # Accept new char
            chars[curr] = 1
            currLen += 1

        if currLen > maxLen:
            # Update max
            maxLen = currLen

    return maxLen

print(longest_substring_with_k_distinct('araaci', 2))   # 4
print(longest_substring_with_k_distinct('araaci', 1))   # 2
print(longest_substring_with_k_distinct('cbbebi', 3))   # 5
print(longest_substring_with_k_distinct('cbbebi', 0))   # 0
