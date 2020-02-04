# Author: Karan Singh Kochar
# Project title: simple coding challenges
# challenge: Reverse a sting

# one line implementation of string reverse.
def strReverse1(s):
    print(" ".join(s.split()[::-1]))

# Detailed implimentation of strings.    
def strReverse2(s):
    i= 0
    length = len(s)
    
    words = []
    while i < length:
        
        # if the charecter is not a space 
        if s[i] != " ":
            
            # starting index 
            startWord = i
            
            # incrementing i till space is found
            while i < length and s[i] != " ":
                i += 1
                
            # addending the word to the list
            words.append(s[startWord: i])
        i+=1
    
    print(" ".join(words[::-1]))
            
            
# test string
s = "you are awesome "
strReverse2(s)
