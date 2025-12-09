class stack:
	def __init__(self):
		self.list_1 = []
		self.min = -1
		self.max = -1

	def status(self):
		print(self.list_1)
		print(self.min)
		print(self.max)

	def push(self,item):
		if self.list_1 == []:
			self.list_1.append(item)
			self.min += 1
			self.max += 1
		else:
			self.list_1.append(item)
			self.max += 1

	def pop(self):
		if self.list_1 == []:
			print("Stack is empty. Pop operation cannot be performed.")
		else:
			result = self.list_1.pop()
			self.max -= 1
		return result


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

operator = ["+","-","*","/","%"]
numerals = ["0","1","2","3","4","5","6","7","8","9"]
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def infix_to_postfix(expression):
	s1 = stack()
	infix_expression = expression
	postfix_expression = []

	for i in infix_expression:
		if i not in operator:
			postfix_expression.append(i)
		else:
			if s1.max == -1:
				s1.push(i)
			else:
				c = s1.list_1[s1.max]
				x=Priority[c]
				y=Priority[i]
				if x >= y :
					z = s1.pop()
					postfix_expression.append(z)
					s1.push(i)
				else:
					s1.push(i)
	else:
		for j in range(len(s1.list_1)):
			z = s1.pop()
			postfix_expression.append(z)
	return postfix_expression

print (infix_to_postfix)
# s1.status()

def solve(opr_1,opr_2,operator):
	if operator == "+":
		temp = int(opr_1) + int(opr_2)
	elif operator == "-":
		temp = int(opr_1) - int(opr_2)
	elif operator == "/":
		temp = int(opr_1) / int(opr_2)
	elif operator == "*":
		temp = int(opr_1) * int(opr_2)
	return temp

def solution():
	s2 = stack()
	expression= main_body() # change this later
	postfix_expression = infix_to_postfix(expression)
	for ele in postfix_expression:
		if ele not in operator:
			s2.push(ele)
		else:
			operand_2=s2.pop()
			operand_1=s2.pop()
			temp = solve(operand_1,operand_2,ele)
			s2.push(temp)
	result = s2.pop()
	return result

expression = main_body()
equation = []
for i in range(len(expression)):
	if expression[i] == "(":
		


result= solution()
print(result)

