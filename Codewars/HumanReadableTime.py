def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds % 3600) // 60
    SS = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(HH,MM,SS)
