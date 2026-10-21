class Solution:
    def isValid(self, s: str) -> bool:
        #Create an empty stack to store opening brackets
        #Create a dictionary to match closing brackets with opening brackets
        #loop through each bracket in the string
        #If it's opening, add to stack
        #if not, check if the stack is empty
        #if empty, return False (nothing matches)
        #Remove the last opening bracker from the stack 
        #check if it matches the closing basket
        #if not, the return false
        #After the loop, check if the stack is empty 

        stack = []

        brackets ={
            ')': '(',
            ']': "[",
            '}': '{'
        }

        for char in s: #for every character in string made above
            if char in brackets.values(): #if char matched the values in the variable brackets
                stack.append(char) #character gets added to the empty stack
            else:
                if not stack:
                    return False #if it comes back as empty, return false

                top = stack.pop() #otherwise, remove the first char from the stack, which we call top
                
                if top != brackets[char]: # if the top doesn't match with the char in brackets return false
                    return False
        
        return len(stack) == 0
            
                