from math import ceil


# buttons: up down eXpress and off
# pushing any button in the off state has no effect
# up: 3 floors up, if cant do nothing
# down: when floor # is odd go down one third of the floors it is on rounded up
# down: if even go down half the floors
# eXpress: go to ground(0) floor, but do nothing when on the halfway floor
# off only works if at ground(0)

# OFF WILL BE STOPPER OF WHILE LOOP

def elevate(floors, commands):
    invalidpresses = 0
    bottom = 0
    halfway = ceil(floors / 2)
    top = floors
    currentfloor = 0
    on = True
    # ---------------------------------------------
    for command in commands:
        if not on:
            # its off
            continue
        if command == 'U':
            if currentfloor + 3 <= top:
                currentfloor += 3
            else:
                invalidpresses += 1
        elif command == 'D':
            if currentfloor == bottom:
                invalidpresses += 1
            elif currentfloor % 2 != 0:
                # Odd floor
                down_floors = ceil(currentfloor / 3)
                currentfloor -= down_floors
                if currentfloor < bottom:
                    currentfloor = bottom
            else:
                # Even floor
                down_floors = currentfloor // 2
                currentfloor -= down_floors
                if currentfloor < bottom:
                    currentfloor = bottom
        elif command == 'X':
            if currentfloor != halfway:
                currentfloor = 0
            else:
                invalidpresses += 1
        elif command == 'O':
            if currentfloor == bottom:
                on = False
                break
            else:
                invalidpresses += 1
        else:
            # Invalid command
            invalidpresses += 1
    print('stopped on floor', currentfloor)
    print('Invalid button presses:', invalidpresses)


elevate(7, ['U', 'U', 'D', 'U', 'X', 'U', 'D', 'O'])
