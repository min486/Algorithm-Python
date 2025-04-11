def solution(sizes):
    max_width = max_height = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        if max_width < a:
            max_width = a
        if max_height < b:
            max_height = b
              
    return max_width * max_height