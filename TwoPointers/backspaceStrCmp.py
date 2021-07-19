"""
LC 844. Backspace String Compare

Given two strings s and t, return true if 
they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

# O(n) time & O(1) space
def nextCharIndex(s, idx):
    bs = 0
        
    while idx >= 0:
        if s[idx] == '#':
            bs += 1
        elif bs > 0:
            bs -= 1
        else:
            break
        idx -= 1
    
    return idx

def backspaceCompareImproved(s, t):
    # Had the right idea, but couldn't quite get my solution to work
    # Referenced solution
    sPoint = len(s) - 1
    tPoint = len(t) - 1
    
    while sPoint >= 0 or tPoint >= 0:
        sCurr = nextCharIndex(s, sPoint)
        tCurr = nextCharIndex(t, tPoint)
        if sCurr < 0 and tCurr < 0:
            return True
        elif sCurr < 0 or tCurr < 0 or s[sCurr] != t[tCurr]:
            return False
        
        sPoint = sCurr - 1
        tPoint = tCurr - 1
            
    return True


# O(n) time, but not O(1) space
def backspaceCompare(s, t):
    # My first simple approach
    revS = s[::-1]
    revT = t[::-1]
    finalS = ''
    finalT = ''
    bs = 0
    
    for char in revS:
        if char == '#':
            bs += 1
        elif bs > 0:
            bs -= 1
            continue
        else:
            finalS += char
    
    bs = 0
    
    for char in revT:
        if char == '#':
            bs += 1
        elif bs > 0:
            bs -= 1
            continue
        else:
            finalT += char
                    
    return finalS == finalT

