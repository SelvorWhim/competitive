# easily adjustable variables depending on game rules:
PORTS = { # snakes and ladders
    2:38, 7:14, 8:31, 15:26, 16:6, 21:42, 28:84, # whoa
    36:44, 46:25, 49:11, 51:67, 62:19, # ouch
    64:60, 71:91, 74:53, 78:98, # so close! Can't fall now!
    87:94, 89:68, 92:88, 95:75, 99:80 # you absolute dastard
}
LAST_SQUARE = 100
N_PLAYERS = 2

class SnakesLadders():

    def __init__(self):
        self.locs = [0] * N_PLAYERS # player locations
        self.turn = 0 # index of player who goes next time play is called; player 1 starts
        self.game_over = False

    def play(self, die1, die2):
        if self.game_over:
            return "Game over!"
        this_turn = self.turn
        new_loc = self.locs[this_turn] + die1 + die2
        if new_loc == LAST_SQUARE:
            self.game_over = True
            return "Player {} Wins!".format(this_turn + 1)
        if new_loc > LAST_SQUARE:
            new_loc = 2*LAST_SQUARE - new_loc # 100-(loc-100) # bounce!
        if new_loc in PORTS: # if snakes/ladders can lead to more snakes/ladders, could change if to while
            new_loc = PORTS[new_loc]
        self.locs[this_turn] = new_loc
        if die1 != die2:
            self.turn = (self.turn + 1) % N_PLAYERS
        return "Player {} is on square {}".format(this_turn + 1, new_loc)
        
# for the record, I hate this game, but nice code challenge
