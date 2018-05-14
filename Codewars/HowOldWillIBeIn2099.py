def calculate_age(year_of_birth, current_year):
    delta = current_year - year_of_birth
    if delta == 0:
        return "You were born this very year!"
    year_s = "year" if abs(delta) == 1 else "years"
    if delta > 0:
        return "You are {} {} old.".format(delta, year_s)
    else:
        return "You will be born in {} {}.".format(-delta, year_s)
