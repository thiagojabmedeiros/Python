def end_other(a, b):
    a = a.lower()
    b = b.lower()
    
    maxS = max(a, b)
    minS = min(a, b)
    
    sz = len(minS)
    
    print(maxS[-sz:], minS)
    if maxS[-sz:] == minS:
        return True
    else:
        return False
  
end_other('Hiabc', 'bc')