# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1867449

# Date: 8/12/2021 
def outcomes():
    '''Prints the total number of outcomes
Last modified 7/12/2021'''
    print(f'\n{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.\n') 

def print_outcome():
    '''Prints the outcome
Last modified 7/12/2021'''
    print(outcome)

credits_pass = 0
credit_defer = 0
credit_fail = 0
progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0

print('''Versions of the Progression outcome program

1. Student version
2. Staff version with Histograms
3. Staff version with Histograms and a list
4. Staff version with Histograms and a text file''')

while True:
    try:
        program = int(input('\nPlease enter needed program: '))
        if program > 0 and program < 5:
            break
        else:
            print('Invalid option')
    except ValueError:
        print('Integer required')

if program == 3:
    data_outputs = []
elif program == 4:
    file = open('Progression_data.txt', 'w')

loop_status = 'y'

while loop_status == 'y':
    while True:
        credits_pass + credit_defer + credit_fail == 120
        while True:
            try:
                credits_pass = int(input('\nPlease enter your credits at pass: '))
                if credits_pass % 20 == 0 and credits_pass < 130:
                    break
                else:
                    print('Out of range')
            except ValueError:
                print('Integer required')

        while True:
            try:
                credit_defer = int(input('Please enter your credit at defer: '))
                if credit_defer % 20 == 0 and credit_defer < 130:
                    break
                else:
                    print('Out of range')
            except ValueError:
                print('Integer required')

        while True:
            try:
                 credit_fail = int(input('Please enter your credit at fail: '))
                 if credit_fail % 20 == 0 and credit_fail < 130:
                     break
                 else:
                    print('Out of range')
            except ValueError:
                print('Integer required')
        if credits_pass + credit_defer + credit_fail != 120:
            print('Total incorrect')
        else:
            break
        
    if credits_pass == 120:
        progress_count += 1
        outcome = 'Progress'
        print_outcome()
        
    elif credit_defer + credit_fail == 20:
        trailer_count += 1 #Progress (module trailer) count
        outcome = 'Module trailer)'
        print('Progress (module trailer)')
        
    elif credit_fail > 79:
        exclude_count += 1
        outcome = 'Exclude'
        print_outcome()
    else:
        retriever_count += 1 #module retriever count
        outcome = 'Module retriever'
        print_outcome()

    if program == 1:
        break       
    all_credits = (f'{credits_pass}, {credit_defer}, {credit_fail}') #For the ease of printing 
    if program == 3:
        data_outputs.append(f'{outcome} - {all_credits}')
    elif program == 4:
        file.write(f'{outcome} - {all_credits}\n')
    
    while True:
            loop_status = input('''\nWould you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')
            if loop_status == 'y' or loop_status == 'q':
                break
            else:
                print('Invalid option')

if program == 4:
    file.close()

if program > 1:
    print('-' * 68)

    print('\nHorizontal Histogram')

    print(f'Progress {progress_count:<3} :', '*' * progress_count)
    print(f'Trailer {trailer_count:<4} :', '*' * trailer_count)
    print(f'Retriever {retriever_count:<2} :', '*' * retriever_count)
    print(f'Excluded {exclude_count:<3} :', '*' * exclude_count)
    outcomes()

    print('-' * 68)

    print('\nVertical Histogram')

    highest_count = max(progress_count, trailer_count, retriever_count, exclude_count)
    print('Progress  Trailer  Retriever  Excluded')

    for x in range(highest_count):
        
        if x < progress_count:
            print(f'{"*":>4}', end = '')
        else:
            print(f'{" ":4}', end = '')
        
        if x < trailer_count:
            print(f'{"*":>10}', end = '')
        else:
            print(f'{" ":>10}', end = '')
        if x < retriever_count:
            print(f'{"*":>10}', end = '')
        else:
            print(f'{" ":10}', end = '')
        if x < exclude_count:
            print(f'{"*":>10}')
        else:
            print(f'{" ":10}')

    outcomes()

if program == 3:
    for i in data_outputs:
        print(i)
    
if program == 4:
    file = open('Progression_data.txt', 'r')
    for line in file:
        print(line, end = '')
    file.close()

    
 

    



