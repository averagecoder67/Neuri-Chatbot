# List of words to type: hi, hello, sup, yo, bye, goodbye, cya, see ya, 5+5, how is your day? (good/bad are options), x, /, +, - (for math) thanks, thanks!, thank you!, thank you
Name = input('(optional) Name: ')

bot_name: str = 'Neuri'
print(f'Hello, {Name}! i\'m {bot_name}! How can I assist you?')

while True:
    user_input: str = input('You: ').lower()
    
    if user_input in ['hi', 'hello', 'sup', 'yo', 'hi!', 'hello!', 'sup!', 'yo!']:
        print(f'{bot_name}: Hello! What do you need help with?')
        
    elif user_input in ['bye', 'goodbye', 'cya', 'see ya', 'see you', 'farewell', 'bye!', 'goodbye!', 'cya!', 'see ya!', 'see you!', 'farewell!']:
        print(f'{bot_name}: See you later!')

    elif user_input in ['How is your day?', 'how\'s your day?']:
        print(f'{bot_name}: Great! how about you?')
        
    elif user_input in ['good', 'great', 'good!', 'great!']:
            print(f'{bot_name}: That\'s nice to hear!')
            
    elif user_input in ['bad', 'terrible', 'bad!', 'Terrible!', 'not good', 'not good!']:
            print(f'{bot_name}: Oh.. Thats not good. Why don\'t you call a friend or start a new project?')
            
    elif user_input in ['i want to commit suicide', 'i want to die', 'i want to kill myself']:
        print(f'{bot_name}: You shouldn\'t, life is worth living. i\'m with you, {Name}.')
        
    elif user_input in ['thanks', 'thanks!', 'thank you!', 'thank you']:
        print(f'{bot_name}: Happy to be of service, {Name}!')
        
    elif user_input in ['add', '+', 'addition']:
        print(f'{bot_name}: lets do some addition!')
        try:
            num1: float = float(input('First Number: '))
            num2: float = float(input('second Number: '))
            print(f'{bot_name}: The sum is: {num1+ num2}')
        except ValueError:
            print(f'{bot_name}: Please insert a valid number.')
            
    elif user_input in ['divide', 'division', '/']:
        print(f'{bot_name}: Okay! Lets do some division!')
        try:
            Dnum1: float = float(input('First Number: '))
            Dnum2: float = float(input('Second Number: '))
            print(f'{bot_name}: The quotient is: {Dnum1 / Dnum2}')
        except ValueError:
            print(f'{bot_name}: Please insert a valid number.')
            
    elif user_input in ['x', '*', 'multiply', 'multiplication']:
        print(f'{bot_name}: Lets do some multiplication!')
        try:
            Mnum1: float = float(input('First Number: '))
            Mnum2: float = float(input('Second Number: '))
            print(f'{bot_name}: The product is: {Mnum1 * Mnum2}')
        except ValueError:
            print(f'{bot_name}: Please insert a valid number.')
            
    elif user_input in ['-', 'subtract', 'Subtraction']:
        print(f'{bot_name}: Lets do some subtraction!')
        try:
            Snum1: float = float(input('First Number: '))
            Snum2: float = float(input('Second Number: '))
            print(f'{bot_name}: The difference is: {Snum1 - Snum2}')
        except ValueError:
            print(f'{bot_name}: Please insert a valid number.')
            
    else:
        print(f'{bot_name}: Sorry, I do not understand. Maybe you spelled something wrong.')
