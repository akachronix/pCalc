print("Welcome to pCalc v0.01.\nby Brendan Gowen\n")
op = input("What operation to you what to perform?")
num1 = float(input("\nPlease enter a number."))
num2 = float(input("\nPlease enter a number."))
addanswer = str(num1 + num2)
subanswer = str(num1 - num2)
mulanswer = str(num1 * num2)
divanswer = str(num1 / num2)
if op == "add" or op == "Add":
	print("\nThe answer is: " + addanswer)
elif op == "subtract" or op == "Subtract":
	print("\nThe answer is: " + subanswer)
elif op == "multiply" or op == "Multiply":
	print("\nThe answer is: " + mulanswer)
elif op == "divide" or op == "Divide":
	print("\nThe answer is: " + divanswer)
print("\nThanks for using pCalc v0.01.")
