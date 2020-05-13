def theRoundTrip(movement):
    left_right = 0
    up_down = 0
    if not ',' in movement:
        return "bad input"

    movement = movement.replace(',', '')
    if not movement.isalpha():
        return "bad input"

    for i in movement:
        if i == 'L':
            left_right -= 1
        elif i == 'R':
            left_right += 1
        elif i == 'U':
            up_down += 1
        elif i == 'D':
            up_down -= 1
        else:
            return "bad input"

    if up_down == 0 and left_right == 0:
        return True
    else:
        return False


inp = input()
print(theRoundTrip(inp))
