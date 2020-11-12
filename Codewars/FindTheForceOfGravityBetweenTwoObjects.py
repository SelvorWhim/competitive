unit_mapper = {
    'kg': 1, 'g': 1e-3, 'mg': 1e-6, 'μg': 1e-9, 'lb': 0.453592,
    'm': 1, 'cm': 1e-2, 'mm': 1e-3, 'μm': 1e-6, 'ft': 0.3048
}

G = 6.67e-11 # no units, we're just using units as scaling factors here

def scaled_unit(a, b, i):
    return a[i] * unit_mapper[b[i]]

def solution(a, b) :
    return G*scaled_unit(a, b, 0)*scaled_unit(a, b, 1)/(scaled_unit(a, b, 2)**2)
