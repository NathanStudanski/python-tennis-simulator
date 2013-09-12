import random
from model import TennisPlayer

def play_game(player1, player2):
    #Function to simulate a single game. The score goes from 0 to 4 instead of from 0 to 40 to simplify.
    score = [0, 0]

    while True:
        if random.random() <= player1.first_serve:
            serving_player = player1.play_first_serve()
            returning_player = player2.play_first_serve_return()
    
        else:
            serving_player = player1.play_second_serve()
            returning_player = player2.play_second_serve_return()
    
        if serving_player == True and returning_player == False:
            score[0] += 1
    
        elif serving_player == False and returning_player == True:
            score[1] += 1
    
        elif serving_player == False and returning_player == False:
            """Next line looks random but I had to compensate when both players fail, and after tons 
            of tests this way gave more accurate results"""
            if random.random() <= 0.275:
                score[0] += 1
        
            else:
                score[1] += 1
            
    
        elif serving_player == True and returning_player == True:
            if random.random() <= 0.5:
                score[0] += 1
        
            else:
                score[1] += 1
        
        if score[0] >= 4:
            break
        
        elif score[1] >= 4:
            break
        
    #This is to implement deuce situations and adventages.
    if score[0] >= 4:
        return player1

    elif score[1] >= 4:
        return player2
    
    elif score[0] == 3 and score[1] == 3:
        score[0] -= 1
        score[1] -= 1
        

def play_set(player1, player2):
    """Function to simulate an entire set, playing games until one of the 
    two players scores 6 games."""
    score = [0, 0]
    
    while True:
        if score[0] >= 6:
            break
    
        elif score[1] >= 6:
            break
            
        for n in range(2):
            if score[0] >= 6:
                break
    
            elif score[1] >= 6:
                break
            
            """This is to rotate the serving order between the two players"""    
            if n == 0:
                if play_game(player1, player2) == player1:
                    score[0] += 1
                else:
                    score[1] += 1
            
            else:
                if play_game(player2, player1) == player1:
                    score[0] += 1
                else:
                    score[1] += 1
        
        """The Tie break is not implemented: Instead of that, the player must win with 
        a difference bigger than 1."""
        if score[0] == 6 and score[0] - score[1] < 2:
            score[0] -= 1
            score[1] -= 1
        
        elif score[1] == 6 and score[1] - score[0] < 2:
            score[0] -= 1
            score[1] -= 1
        
        
    if score[0] == 6:
        return player1
    
    if score[1] == 6:
        return player2
                
    
def play_match(number_of_sets, player1, player2):
    score = [0, 0]
    for n in range(number_of_sets):
        if n % 2 == 0:
            if play_set(player1, player2) == player1:
                score[0] += 1
            
            else:
                score[1] += 1
        
        else:
            if play_set(player2, player1) == player2:
                score[1] += 1
            
            else:
                score[0] += 1
    if score[0] > score[1]:
        return 1
    
    else:
        return 2
