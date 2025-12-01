def total_length_paint(a, b, c, d):
    
    if b < c or d < a:
        return abs(a - b) + abs(c - d)
    else:
        return max(b, d) - min(a, c)

total_length_paint(a, b, c, d)