# arithmatic expression

operator = ["+","-","*","/","%"]
numerals = ["0","1","2","3","4","5","6","7","8","9"]

def main_body() :
	user_input = input("Input aritmatic expression :")
	expression = []
	term = ""

	for i in user_input :
		if i in operator :
			expression.append(term)
			expression.append(i)
			
			term = ""
		else :
			term = term + i
	else :
		expression.append(term)

	return expression

def validation():
	expression = main_body()
	for i in range (len(expression)) :
		if i%2 == 0 :
			if not expression[i].isnumeric() :
			# if expression[i] not in numerals :
				return "Not a valid expression"
		elif i%2 != 0 :
			if expression[i] not in operator :
				return "Not a valid expression" 
	return expression

"""def validation():
 	expression = main_body()
	
 	for i in range (0,len(expression),2) :
 		if not expression[i].isnumeric() :
 			return "Not a valid expression"
			  
 	for j in range(1,len(expression)-1,2):
		if expression[j] not in operator:
			return "Not a valid operator"
 	return expression"""

print(validation())
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
	 
	 
def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in expression:

        if character not in operator:  # if an operand append in postfix expression

            output+= character

        # elif character=='(':  # else Operators push onto stack

        #     stack.append('(')

        # elif character==')':

        #     while stack and stack[-1]!= '(':

        #         output+=stack.pop()

        #     stack.pop()

        else: 

            while Priority[character]<=Priority[stack[-1]]: #stack and stack[-1]!='(' and :

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output


expression = input('Enter infix expression ')

print('infix notation: ',expression)

print('postfix notation: ',infixToPostfix(expression))