#Import random package to generate random numbers
import random

#function to generate random integers between a range i.e min,max
def random_integer(min, max):
    """
    Random integer generation.
    """
    return random.randint(min, max)

#function to randomly select the arithmetic operator
def random_operator():
    '''Randomly selects an operator'''
    return random.choice(['+', '-', '*'])

#function to calcular the random numbers +,- and * is  supported
def calculator(number1, number2, operator):
    '''Creates a question and add in the variable problem'''
    problem = f"what is {number1} {operator} {number2} ?"
    '''Caclulating the numbers accordingly to the operator'''
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return problem, answer

#This function will create the game and utilize the above functions random_integer,random_operator,calculator
def math_quiz():
    '''Score to be incremented on every correct answer'''
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    '''present the random questions total_questions number of times'''
    for _ in range(total_questions):
        number1 = random_integer(1, 10); number2 = random_integer(1, 10); operator = random_operator()
        PROBLEM, ANSWER =calculator(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Please enter your answer: ")
        useranswer = int(useranswer)
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            '''Increment to user's total score'''
            score +=1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    '''Finally, print the total score'''
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    try:
        math_quiz()
    except:
        print("Please enter a valid value")

    
