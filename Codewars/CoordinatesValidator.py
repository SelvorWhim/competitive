def is_valid_coordinates(coords):
    try:
        assert("e" not in coords.lower()) # some strings with e are valid formats of float but not coordinates
        lat,lng = (float(coord) for coord in coords.split(",")) # otherwise, just check that the coordinates can be converted to float (spaces between sign and digits don't work, whitespace at the edges is fine)
        return abs(lat) <= 90 and abs(lng) <= 180 # and in the right range
    except:
        return False
