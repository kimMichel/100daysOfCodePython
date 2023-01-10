# def - Function
def turn_left():
    print("turn_left")

def move():
    print("move")

def front_is_clear():
    print("if front is clear: true/false")

def right_is_clear():
    print("check if righ is clear: true/false")

def at_goal():
    print("conditional if came at goal: true/false")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# while - estrutura de repeticao
while front_is_clear():
    move()

turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear:
        move()
    else:
        turn_left()