def to_rna(dna_strand):
    equivalences = {
        "G" : "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    result = ""
    for char in dna_strand:
        result += equivalences[char]

    return result