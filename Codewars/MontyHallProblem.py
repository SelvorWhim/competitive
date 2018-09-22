# idea: people who guessed correctly at first will lose by switching, the rest will win
def monty_hall(correct_door_number, participant_guesses):
    win_rate = sum(1 for guess in participant_guesses if guess != correct_door_number)/len(participant_guesses)
    return round(100*win_rate)
