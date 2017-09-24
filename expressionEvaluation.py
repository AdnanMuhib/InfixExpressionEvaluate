


# method to evaluate given mathematical expression
def evluate_expression(expression):
	
	# removing spaces in the expression
	expression = expression.replace(" ","")
	
	# array to store the numerical values and operators in same order as entered by the user
	arr = []
	op = ""
	for i in xrange(len(expression)):
		
		if (is_number(expression[i])):
			op += expression[i]
		elif(is_operator(expression[i])):
			if not(op == ""):
				arr.append(op)
				op = ""
			arr.append(expression[i])
	if not(op == ""):
		arr.append(op)
		op = ""
	# now arr has every numerical value and operators in the same sequence as entered by the user
	print(arr)
	
	# stack for the numerics
	numerics = []
	# stack for the operators
	operators = []
	# logic for evaluating the arr using stack
	for i in range(len(arr)):
		if (is_number(arr[i])):
			numerics.append(float(arr[i]))
		elif (arr[i] == '('):
			operators.append(arr[i])
		elif (is_operator(arr[i])):
			while not(precendence(arr[i] >= precendence[operators[0]])):
				 op = operators.pop()
				 op2 = numerics.pop()
				 op1 = numerics.pop()
				 numerics.append(calculate(op, op1, op2))
			operators.append(arr[i])
		elif (arr[i] == ')'):
			while (operators[0] != '('):
				op = operators.pop()
				op2 = numerics.pop()
				op1 = numerics.pop()
				numerics.append(calculate(op, op1, op2))
	while(len(operators) != 0):
		op = operators.pop()
		op2 = numerics.pop()
		op1 = numerics.pop()
		numerics.append(calculate(op, op1, op2))	
	print(numerics[0])
	return numerics[0]


# method to check the operators precedence
def precendence(operator):
	if (operator == '/' or operator == '*'):
		return 2
	if (operator == '+' or operator == '-'):
		return 1
	return 0

# method to check if the given input is an operators
def  is_operator(character):
	ops = ['+', '-', '/', '*']
	for i in range(len(ops)):
		if(character == ops[i]):
			return True
	return False

# method to check whether a character is number 
def is_number(character):
	if (character.isdigit()):
		return True
	return False
# method to perform calculation
def calculate(op, op1, op2):
	if(op == '+'):
		return float(op1 + op2)
	if(op == '-'):
		return float(op1 - op2)
	if(op == '*'):
		return float(op1 * op2)
	if(op == '/'):
		if(op2 != 0):
			return float(op1 / op2)
		return 0
	return 0
# main function 
def main():
	expression = raw_input("Enter a mathematical expression\n i.e (1*2) / 5 - 3 * 1 :")
	result  = evluate_expression(expression)
	return

# driver for the main function
if __name__ == '__main__':
	main()
