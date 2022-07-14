def is_ascending(lst: List[int]) -> bool:
    ''' determine if the given list of ints is in strict ascending order'''

    return all(a<b for a,b in zip(lst, lst[1:]))

