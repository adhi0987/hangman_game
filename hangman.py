import hangman_stages
import words_directory
import random
lives=9
chosen_words=random.choice(words_directory.words)
display=[]
for letter in range(len(chosen_words)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input('Enter a letter:').lower()
    for position in range(len(chosen_words)):
        alphabet=chosen_words[position]
        if(guessed_letter==alphabet):
            display[position]=guessed_letter
    if guessed_letter not in chosen_words:
        lives-=1
        if(lives==0):
            game_over=True
            print('YOU LOSE PLEASE TRY AGAIN')
        print(hangman_stages.stages[lives])
    if '_' not in display:
        game_over=True
        print('YOU Won Congratulations')
        str=''
        print('The Word  is ->',str.join(display))
        break
    print('no of lives left:',lives)
    print(display)       
