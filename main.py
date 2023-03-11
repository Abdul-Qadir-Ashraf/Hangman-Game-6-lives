from random import choice
list_of_words = ['army', 'beautiful', 'became', 'if', 'actually','generates','random','words', 'for', 'use', 'as', 'sampletext']
wrong_letters = []
correct_letters = []
lives = 6
right_answer = 0
game_over = False



def secret(listofwords):
    secret_word = choice(listofwords)
    different_letters = len(set(secret_word))
    return secret_word, different_letters

def userinput():
    user_input = ''
    limit = 'abcdefghijklmnopqrstuvwxyz'
    is_valid = False
    while not is_valid:
        user_input = input("Enter only one letter of alphabet: ")

        if user_input in limit and len(user_input) == 1:
            is_valid = True
        else:
            print("You have given an invalid input,Enter only one letter of alphabet: ")
    return user_input

def printing_of_dash(secret):
    hidden_list = []
    for l in secret:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('_')
    print("".join(hidden_list))

def checking(user_input,secret,lives,matches):
    end = False

    if user_input in secret and secret not in correct_letters:
        correct_letters.append(user_input)
        print("You have guessed the correct letter")
        matches +=1
    elif user_input in secret and secret in correct_letters:
        print("You have already guessed this letter\n")
    else:
        lives-=1
        print(f'Oops, you have guessed the wrong letter,{lives} left\n')
        wrong_letters.append(user_input)
    if lives == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(secret)
    return lives,end,matches

def lose():
    print("You don't have any tries left")
    print(f'The hidden word was {secret}')
    return True

def win(secret):
    printing_of_dash(secret)
    print("congratulations, You won")
    return True



hidden_word,unique_letters = secret(list_of_words)
while not game_over:
    printing_of_dash(hidden_word)
    print('\n')
    user_input = userinput()
    lives,end,right_answer = checking(user_input,hidden_word,lives,right_answer)
    game_over = end
