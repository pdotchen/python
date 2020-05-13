def checkLights(lights):
    counter = 0
    large_counter = 0

    for i in lights:
        if i == '1':
            counter += 1
            if counter > large_counter:
                large_counter = counter
        else:
            counter = 0

    return large_counter


l = str(input())
print(checkLights(l))
