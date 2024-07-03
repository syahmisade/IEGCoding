'''
Baca balik lepas ni!!!
Parse and evaluate simple math word problems returning the answer as an integer.

What is 5?    -> 5
What is 5 plus 13?    -> 13
What is 7 minus 5?    -> 2
What is 6 multiplied by 4?     -> 24
What is 25 divided by 5?       -> 5
What is 5 plus 13 plus 6?      -> 24
What is 3 plus 2 multiplied by 3?       -> 15
'''
# def mathTranslater(statement):
#     statement = statement.lower().strip()
#     statement = statement.replace('plus', '+')
#     statement = statement.replace('minus', '-')
#     statement = statement.replace('multiplied by', '*')
#     statement = statement.replace('divided by', '/')
    
#     if "what is " in statement and "? " in statement:
#         statement = statement.replace("what is ", "")
#         statement = statement.replace("?", "")
    
#     try:
#         return print(f"-> {int(eval(statement))}")
#     except Exception as e:
#         return print(f"Error found: {e}")
        
# statement = input("Enter a statement: \n")
# mathTranslater(statement)

def evaluate_math_problem(problem):
    problem = problem.lower().strip()
    if problem.startswith("what is ") and problem.endswith("?"):
        problem = problem[8:-1]

    problem = problem.replace("plus", "+")
    problem = problem.replace("minus", "-")
    problem = problem.replace("multiplied by", "*")
    problem = problem.replace("divided by", "/")
    
    # Evaluate the expression using eval safely
    try:
        result = eval(problem)
        return int(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function with the given problems
test_problems = [
    "What is 5?",
    "What is 5 plus 13?",
    "What is 7 minus 5?",
    "What is 6 multiplied by 4?",
    "What is 25 divided by 5?",
    "What is 5 plus 13 plus 6?",
    "What is 3 plus 2 multiplied by 3?"
]

for problem in test_problems:
    print(f"{problem} -> {evaluate_math_problem(problem)}")
