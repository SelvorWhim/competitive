from math import ceil

def declare_winner(fighter1, fighter2, first_attacker):
    turns_to_win = [ceil(fighter2.health / fighter1.damage_per_attack), ceil(fighter1.health / fighter2.damage_per_attack)]
    first_attacker_i = 0 if first_attacker == fighter1.name else 1
    turns_to_win[first_attacker_i] -= 0.5 # simple way to represent first turn advantage without extra conditionals
    return fighter1.name if turns_to_win[0] < turns_to_win[1] else fighter2.name
