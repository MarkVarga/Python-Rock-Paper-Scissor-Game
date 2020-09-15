#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def game():
    print('Welcome to Rock, Paper, Scissor Game!')
    game_on = input('Would you like to play? Press "Y" for Yes or "N" for No: ')
    
    if game_on.lower() == "y":
        game_on = True
    elif game_on.lower() == "n":
        game_on = False
        print('See you later!')
    else:
        print('Invalid answer! Please try again!')
        return game()
    
    draw = 0
    win = 0
    computer_win = 0
    rounds = 0
    
    while game_on:
        player_input = input('Do you choose Rock, Paper or Scissors? Press R, P or S: ')
        choices = ["r","p","s"]
        computer_choice = random.choice(choices)
        result = f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}'
        
        
        if player_input.lower() not in ('r','p','s'):
            print('Invalid answer! Please enter R for Rock, P for Paper or S for Scissor!')
            continue 
        
        elif player_input.lower() == computer_choice.lower():
            draw += 1
            rounds += 1
            print(player_input +' vs '+ computer_choice)
            print('Draw!')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')
            
        elif player_input.lower() == "r" and computer_choice.lower() == "p":
            computer_win += 1
            rounds += 1
            print(player_input +' vs '+ computer_choice)
            print('Computer Wins!')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')
        elif player_input.lower() == "p" and computer_choice.lower() == "s":
            computer_win += 1
            rounds += 1
            print(player_input +' vs '+ computer_choice)
            print('Computer Wins!')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')
        elif player_input.lower() == "s" and computer_choice.lower() == "r":
            computer_win += 1
            rounds += 1
            print(player_input +' vs '+ computer_choice)
            print('Computer Wins')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')
        else:
            win += 1
            rounds += 1
            print(player_input +' vs '+ computer_choice)
            print('Player Wins!')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')    
            
        play_again = input('Would you like to play again? Y or N?: ')

        if play_again.lower() == "y":
            continue
        else:
            print('Thanks for playing!')
            print(f'Round: {rounds} | Wins: {win} | Draws: {draw}  | Computer wins: {computer_win}')
        break    


# In[4]:


game()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




