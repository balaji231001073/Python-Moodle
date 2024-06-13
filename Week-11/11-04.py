Develop a Python program that safely performs division between two numbers provided by the user. Handle exceptions like division by zero and non-numeric inputs.

Input Format: Two lines of input, each containing a number.

Output Format: Print the result of the division or an error message if an exception occurs.





For example:

Input            	Result

10                5.0

2	

10                Error: Cannot divide or modulo by zero.

0	


ten              Error: Non-numeric input provided.

5

	




Coding:

def main():

    try:

        num1 = float(input())

        num2 = float(input())

       

        division_result = num1 / num2

        modulo_result = num1 % num2

       

        print(division_result)

        

    except ValueError:

        print("Error: Non-numeric input provided.")

    except ZeroDivisionError:

        print("Error: Cannot divide or modulo by zero.")
