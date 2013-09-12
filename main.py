from simulator import *
def main():
    Player1 = 0
    Player2 = 0 

    player1 = TennisPlayer(float(input('Player 1 - % First Serve: ')),float(input('Player 1 - % First Serve Points Won: ')), float(input('Player 1 - % Second Serve Points Won: ')), float(input('Player 1 - % First Serve Return Points Won: ')),  float(input('Player 1 - % Second Serve Return Points Won: ')))
    player2 = TennisPlayer(float(input('Player 2 - % First Serve: ')),float(input('Player 2 - % First Serve Points Won: ')), float(input('Player 2 - % Second Serve Points Won: ')), float(input('Player 2 - % First Serve Return Points Won: ')),  float(input('Player 2 - % Second Serve Return Points Won: ')))

    number_of_simulations = int(input('How many simulations do you want to reproduce? '))
    number_of_sets = int(input('How many sets for each match? '))

    for n in range(number_of_simulations):
        if play_match(number_of_sets, player1, player2) == 1:
            Player1 += 1

        else:
            Player2 += 1

    print "Player 1 won " + str(Player1) + " - " + str(float(Player1)/number_of_simulations) + "%"
    print "Player 2 won " + str(Player2) + " - " + str(float(Player2)/number_of_simulations) + "%"


if __name__ == "__main__":
    main()