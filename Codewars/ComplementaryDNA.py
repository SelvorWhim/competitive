complement = {"A":"T", "T":"A", "C":"G", "G":"C"}

def DNA_strand(dna):
    return "".join([complement[l] for l in dna])
