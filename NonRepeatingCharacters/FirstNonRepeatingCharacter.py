def find_first_non_repeated_char(sequence: str):
    lower_case = sequence.lower()
    for c, i in lower_case:
        if lower_case.count(c) == 1:
            return sequence[i]
    
    return None




print(find_first_non_repeated_char("S"))
