

# "Lame Game" beginning
# This program present game options to the user, prompt for a selection
# and then execute the selection. This program will continue to prompt
# for a user choice until the user quits.

import random

def main():

    # Initialize menu option
    user_choice = menu()

    # Loops until user quits program
    while user_choice != 7:

        # User Choice 1 goes to 'Make Change'
        if user_choice == 1:
            print ('You selected Make Change.')
            print()
            make_change()
            print()
        # User Choice 2 goes to 'High Card'
        elif user_choice == 2:
            print ('You selected High Card.')
            print()
            high_card()
            print()
        # User Choice 3 goes to 'Deal Hand'
        elif user_choice == 3:
            print ('You selected Deal Hand.')
            print()
            deal_hand()
            print()
        # User Choice 4 goes to 'Save Dream Hand'
        elif user_choice == 4:
            print ('You selected Save Dream Hand')
            print()
            save_dream_hand()
            print()
        # User Choice 5 goes to 'Display Dream Hand'
        elif user_choice == 5:
            print ('You selected Display Dream Hand')
            print()
            display_dream_hand()
            print()
        # User Choice 6 goes to 'Word Guess'
        elif user_choice == 6:
            print ('You selected Word Guess.')
            print()
            word_guess()
            print()
        # Reprompt for new selection    
        user_choice = menu()

# Display the menu and check if user entered a valid choice
def menu():
    # Display menu options
    print('Your options are as follows:')
    print('\t',"1. Make Change")
    print('\t',"2. High Card")
    print('\t',"3. Deal Hand")
    print('\t',"4. Save Dream Hand")
    print('\t',"5. Display Dream Hand")
    print('\t',"6. Word Guess")
    print('\t',"7. Quit")

    # Prompt user to select an option
    user_choice = int(input('Please enter your selection: '))

    # Validate user selection
    while user_choice < 1 or user_choice > 7:
        print()
        print ('INVALID OPTION')

    # If selection is valid, return the choice
    return (user_choice)
    
    
# Calculate and display change owed to customer
def make_change():
    # Get amount owed and amount paid
    amount_owed = float(input('How much does the customer owe? $'))
    amount_paid = float(input('How much did the customer pay? $'))

    # Calculate amount paid versus amount owed
    # Provide error if amount paid is not enough
    if amount_paid < amount_owed:
        print ('The customer did not give enough money.')

    # Otherwise, calculate and display the change owed
    else:
        change_due = amount_paid - amount_owed
        print ('The amount of change for the customer is: $', format(change_due, ",.2f"), sep="")

        # Calculate dollars owed
        if change_due > 1.00:
            dollars = int(change_due / 1.00)
            print ('The customer is owed', dollars, 'dollars')
            change_due = change_due % dollars

        # Calculate quarters owed
        if change_due >= 0.25:
            quarters = int(change_due / 0.25)
            print ('The customer is owed', quarters, 'quarters')
            change_due = change_due % 0.25

        # Calculate dimes owed
        if change_due >= 0.10:
            dimes = int(change_due / 0.10)
            print ('The customer is owed', dimes, 'dimes')
            change_due = change_due % 0.10

        # Calculate nickels owed
        if change_due >= 0.05:
            nickels = int(change_due / 0.05)
            print ('The customer is owed', nickels, 'nickels')
            change_due = change_due % 0.05

        # Calculate pennies owed
        if change_due > 0:
            pennies = int(change_due / 0.009)
            print ('The customer is owed', pennies, 'pennies')
            change_due = change_due % 0.01

# Deal cards to two players and determine/display winner
def high_card():

    # Prompt for and read players' names
    user_1 = input('Enter the first player\'s name: ')
    user_2 = input('Enter the second player\'s name: ')

    # Randomly generate card values
    card_1 = random.randint(1,13)
    card_2 = random.randint(1,13)

    # Display the player names and their card's face value
    print (user_1, 'was dealt:', end=" "), display_face_value(card_1)
    print (user_2, 'was dealt:', end=" "), display_face_value(card_2)

    # Calculate and display victor
    # Cehck for player one victory
    if card_1 > card_2:
        print (user_1, 'is the winner!')
    # Check for player two victory
    elif card_2 > card_1:
        print (user_2, 'is the winner!')
    # Check for a tie
    else:
        print ('It\'s a tie!')

# Print face value of the dealt cards based on the random number;
def display_face_value(value):
    if value == 1:
        print ('Ace')
    elif value == 2:
        print ('Two')
    elif value == 3:
        print ('Three')
    elif value == 4:
        print ('Four')        
    elif value == 5:
        print ('Five')        
    elif value == 6:
        print ('Six')       
    elif value == 7:
        print ('Seven')        
    elif value == 8:
        print ('Eight')        
    elif value == 9:
        print ('Nine')
    elif value == 10:
        print ('Ten')        
    elif value == 11:
        print ('Jack')        
    elif value == 12:
        print ('Queen')     
    elif value == 13:
        print ('King')       

# Deal Hand to Player
def deal_hand():

    # Create hand_list list
    hand_list = []

    # Randomly generate card values and store them to hand_list 
    card_1 = random.randint(1,13)
    hand_list.append(card_1)
    card_2 = random.randint(1,13)
    hand_list.append(card_2)
    card_3 = random.randint(1,13)
    hand_list.append(card_3)
    card_4 = random.randint(1,13)
    hand_list.append(card_4)
    card_5 = random.randint(1,13)
    hand_list.append(card_5)

    # Pass hand_list to display_hand()
    display_hand(hand_list)

    # Pass hand_list to hand_stats()
    hand_stats(hand_list)
        
# Save Dream Hand saves the user's selected hand into a file
def save_dream_hand():
    print ('You get to build your dream hand of 5 cards! \nAce (1) is low, and King (13) is high.')

    # Create dream_hand list
    dream_hand = []
    
    try:
        # Get user's card choice, validate card, and add value to dream_hand list
        dream_1 = int(input('Enter the value of your first card: '))
        while dream_1 < 1 or dream_1 > 13: 
            dream_1 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_1)
        
        dream_2 = int(input('Enter the value of your second card: '))
        while dream_2 < 1 or dream_2 > 13: 
            dream_2 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_2)

        dream_3 = int(input('Enter the value of your third card: '))
        while dream_3 < 1 or dream_3 > 13: 
            dream_3 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_3)

        dream_4 = int(input('Enter the value of your fourth card: '))
        while dream_4 < 1 or dream_4 > 13: 
            dream_4 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_4)

        dream_5 = int(input('Enter the value of your last card: '))
        while dream_5 < 1 or dream_5 > 13: 
            dream_5 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_5)
      
        # Prompt and read user choice for filename
        print()
        filename = str(input('Please name the file to be saved: '))
        # Open the file for writing
        outfile = open(filename, 'w')
        # Write user's card choices to the file
        for line in dream_hand:
            line = str(line) + '\n'
            outfile.write(line)
        # Close the file
        outfile.close()

        print ('Your dream hand was saved to ', filename, '.', sep='')

    except ValueError:
        print()
        print('ERROR: You must enter a number from 1 to 13.')
                        
    
# Display Dream Hand reads the user's selected file and
# displays the face value of the stored values
def display_dream_hand():

    # Create display_dream_hand list
    dream_hand = []

    try: 
        # Prompt and read the filename to open
        filename = str(input('Enter the name of the file you want to display: '))
        print()
        # Open the file for reading
        infile = open(filename, 'r')
        # Read and add lines to display_dream_hand list
        for line in infile:
            # Convert line to integer and remove newline character
            line = int(line.rstrip('\n'))
            # Add line to dream_hand list
            dream_hand.append(line)
        # Close the file
        infile.close()

        display_hand(dream_hand)
        
    except FileNotFoundError:
        print ('Error: The file \'',filename, '\' was not found.', sep='')

# Display Hand accepts a list as input and passes
# the items one at a time to display_face_value()
def display_hand(a_list):
    for item in a_list:
        display_face_value(item)

# Hand Stats takes a list and displays the highest and lowest cards.
# It shows the total value of the cards added together as well as the
# average value of the cards in the hand.
def hand_stats(a_list):
    print()
    highest_card = max(a_list)
    lowest_card = min(a_list)
    print('Highest card value: ', highest_card)
    print('Lowest card value: ', lowest_card)

    # Calculate the total value of cards
    total = 0
    for item in a_list:
        total += item
    print ('The total card value is ', total, '.', sep='')

    # Calculate and display the average value of cards
    list_length = len(a_list)
    average = total / list_length
    print ('The average card value is ', average, '.', sep='')

# Word Guess accepts a word from the user and allows user to guess
# the word one letter at a time.
def word_guess():
    # Prompt for and read user's word
    word = input('Please provide your secret word: ')
    print ('\n' * 100)

    # Create guess_word list to track correct guesses
    guess_word = []
    final_answer = ''
    for letter in word:
        guess_word.append('*')
        final_answer += ('*')
    length = len(guess_word)

    # Create guessed_list to track all guesses
    guessed_list = []

    # Continue running until the word is guessed
    while final_answer != word:
        final_answer = ''
        print()
        guess = input('Guess a letter that is in the word: ')

        # Check guessed letter against guessed_list
        if guess in guessed_list:
            print ('The letter \'', guess, '\' has already been guessed.', sep='')           
        else:
            # If letter has not been guessed, add it to the guessed_list
            guessed_list.append(guess)
            # If the guess is correct, display message
            if guess in word:
                print ('Good guess!')
                # Add correct letters into guess_word
                for num in range(0, length):
                    if guess == word[num]:
                        guess_word[num] = guess
            else:
                print ('The letter \'', guess, '\' is not in the word.',sep='')

        # Update final_answer for while loop
        for num in range(0, length):
            final_answer += guess_word[num]

        # Display the word so far
        print ('The word so far is:', final_answer)

    # Display victory message
    print ('Congratulations! You guessed the word!')

main()
