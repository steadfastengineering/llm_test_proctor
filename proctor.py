import json
import argparse
import os 

class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"   
    BLUE = "\033[34m"   
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
     
def get_questions(file):
    with open(file) as f:
        return json.load(f)

def clear_previous_lines(num_lines):
    for _ in range(num_lines):
        # Move the cursor up one line
        print('\033[F', end='')
        # Clear the line
        print('\033[K', end='')

def print_question(question):
    print(f'{question['id']}. {question['question']}')
    print()
    print(f'\ta. {question['a']}')
    print(f'\tb. {question['b']}')
    print(f'\tc. {question['c']}')
    print(f'\td. {question['d']}')
    print() 


def print_start_message(file, total):
    print(f'{Colors.GREEN}Proctoring {file}{Colors.RESET}')
    print(f'{Colors.YELLOW}{total}{Colors.RESET} Questions')
    print(f'Enter {Colors.RED}\'q\'{Colors.RESET} to quit')
    print()
    

def proctor(file):
    grade = 0
    total = len(get_questions(file)['questions']) 
    print_start_message(file, total)
    
    for question in get_questions(file)['questions']:
        print_question(question)
        answer = input(f'{Colors.CYAN}Your answer: ')
        print(f'{Colors.RESET}')
        clear_previous_lines(9)
        if answer == 'q':
            break
        elif answer == question['answer']:
            grade += 1
    
    print(f'{Colors.MAGENTA}Your grade is {grade}/{total}.{Colors.RESET}')
    print()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proctor and grade questions from a JSON file having \'quiz format\'.")
    parser.add_argument('json_file', type=str, help="Path to JSON file.")
    args = parser.parse_args()
    proctor(args.json_file) 