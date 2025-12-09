class Stack():
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
			print('Stack is empty. Pop opearion cannot be performed')
		else:
			result = self.list_1.pop()
			self.max -= 1
		return result



operators = ['-','+','/','*']
numbers = ['1','2','3','4','5','6','7','8','9','0']
Priorities = {'-':1,'+':1,'*':2,'/':2,'^':3}

def equation_generator():
	user_eq = input("enter the equation: ")
	expression = []
	item = ''
	
	for i in range(len(user_eq)):
		if user_eq[i] == '-' and i == 0:
			item += user_eq[i]
		elif user_eq[i] == '-' and user_eq[i-1] in operators:
			item += user_eq[i]

		elif user_eq[i] not in operators:
			item = item + user_eq[i]
		elif user_eq[i] in operators and i == 0:
			print('Invalid equation')
			# expression.append(user_eq[i])
			break
		else:
			expression.append(item)
			expression.append(user_eq[i])
			item = ''
	else:
		expression.append(item)
	# print(expression)
	return expression

def validation():
	expression = equation_generator()
	for i in range(len(expression)):
		if i % 2 == 0:
			if not expression[i].isnumeric():
				return 'Not a valid equation'
			elif i%2 != 0:
				if expression[i] not in operators:
					return 'Not a valid equation'
			else:

				return 'Valid Equation.'
	return expression

print(validation())


s1 = Stack()
infix_expression = equation_generator()
postfix_expression = []

for i in infix_expression:
	if i not in operators:
		postfix_expression.append(i)
	else:
		if s1.max == -1:
			s1.push(i)
		else:
			a = s1.list_1[s1.max]
			b = Priorities[a]
			c = Priorities[i]
			if b >= c:
				d = s1.pop()
				postfix_expression.append(d)
				s1.push(i)
			else:
				s1.push(i)
else:
	for j in range(len(s1.list_1)):
		d = s1.pop()
		postfix_expression.append(d)

print(postfix_expression)

def solve(opr_1,opr_2,operators):
	temp =''
	if operators == '+':
		temp = int(opr_1) + int(opr_2)
	elif operators == '-':
		temp = int(opr_1) - int(opr_2)
	elif operators == '*':
		temp = int(opr_1) * int(opr_2)
	elif operators == '/':
		temp = int(opr_1) / int(opr_2)
	return temp

s2 = Stack()
for element in postfix_expression:
	if element not in operators:
		s2.push(element)
	else:
		operand_2 = s2.pop()
		operand_1 = s2.pop()
		temps = solve(operand_1,operand_2,element)
		s2.push(temps)
result = s2.pop()
print(result)













# def Infix_to_Postfix(expression):
# 	stack = [] # intialization of an empty stack

# 	output = []

# 	for i in expression:
# 		if i not in operators:
# 			output.append(i)
# 		else:
# 			if stack == []:
# 				stack.append(i)
# 			else:
# 				while stack and Priorities[i] <= Priorities[stack[-1]]:
# 					output.append(stack.pop())	
# 				stack.append(i)
# 	while stack:
# 		output.append(stack.pop())
# 	# output_lst = list(output)
# 	return output

# def solve(expression):
# 	pass

# a = equation_generator()
# print("infix notation: ",a)
# print('postfix notation: ',Infix_to_Postfix(a))
# # print('Solution od notation:',solve(a))

