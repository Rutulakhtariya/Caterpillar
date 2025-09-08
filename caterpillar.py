# import random
# import turtle as t
# t.bgcolor('yellow')
# caterpillar = t.Turtle()
# caterpillar.shape('square')
# caterpillar.color('red')
# caterpillar.speed(0)
# caterpillar.penup()
# caterpillar.hideturtle()
# leaf = t.Turtle()
# leaf_shape = ((0,0), (14,2), (18,6), (20,20), \
#              (6,18), (2,14))
# t.register_shape('leaf',leaf_shape)
# leaf.shape('leaf')
# leaf.color('green')
# leaf.penup()
# leaf.hideturtle()
# leaf.speed(0)
# game_started = False
# text_turle = t.Turtle()
# text_turle.write('PRESS SPACE TO START',align='center',\
#                    font=('Arial',16, 'bold'))
# text_turle.hideturtle()
# score_turtle = t.Turtle()
# score_turtle.hideturtle()
# score_turtle.speed(0)
# def outside_window();
#     pass
# def game_over():
#     pass
# def display_score(current_score):
#     pass
# def place_leaf():
#     pass
# def start_game():
#     global game_started
#     if game_started:
#         return
#     game_started = True
#     score = 0
#     text_turle.clear()
#     caterpillar_speed = 2 
#     caterpillar_length = 3
#     caterpillar.shapesize(1, caterpillar_length, 1)
#     caterpillar.showturtle()
#     display_score(score)
#     place_leaf()
#     while True:
#         caterpillar.forward(caterpillar_speed)
#         if caterpillar.distance(leaf) < 20:
#             place_leaf()
#             caterpillar_length = caterpillar_length + 1
#             caterpillar.shapesize(1, caterpillar_length, 1)
#             caterpillar_speed = caterpillar_speed + 1
#             score = score + 10
#             display_score(score)
#         if outside_window():
#             game_over()
#             break
# t.onkey(start_game,'space')
# t.listen()
# t.mainloop()
# def outside_window():
#     left_wall = -t.window_width() / 2 
#     right_wall = t.window_width() / 2
#     top_wall = t.window_height() / 2
#     bottom_wall = -t.window_height() / 2
#     (x, y) = caterpillar.pos()
#     outside = \
#             x< left_wall or \
#             x> right_wall or \
#             y< bottom_wall or \
#             y> top_wall
#     return outside
# def game_over():
#  caterpillar.color('yellow')
#  leaf.color('yellow')
#  t.penup()
# def outside_window():
#  left_wall = -t.window_width() / 2
#  right_wall = t.window_width() / 2
#  top_wall = t.window_height() / 2
#  bottom_wall = -t.window_height() / 2
#  (x, y) = caterpillar.pos()
#  outside = \
#  x< left_wall or \
#  x> right_wall or \
#  y< bottom_wall or \
#  y> top_wall
#  return outside
# def game_over():
#     caterpillar.color('yellow')
#     leaf.color('yellow')
#     t.penup()
#     t.hideturtle()
#     t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))
# def display_score(current_score):
#     score_turtle.clear()
#     score_turtle.penup()
#     x = (t.window_width() / 2) - 50
#     y = (t.window_height() / 2) - 50
#     score_turtle.setpos(x, y)
#     score_turtle.write(str(current_score), align='right', \ 
#                         font=('Arial', 40, 'bold'))
# def place_leaf():
#     leaf.ht()
#     leaf.setx(random.randint(-200, 200))  
#     leaf.sety(random.randint(-200, 200))
#     leaf.st() 
#     game_over()
#     break
# def move_up():
#     if caterpillar.heading() == 0 or caterpillar.heading() == 180:
#         caterpillar.setheading(90)
# def move_down():
#     if caterpillar.heading() == 0 or caterpillar.heading() == 180:
#         caterpillar.setheading(270) 
# def move_left():
#     if caterpillar.heading() == 90 or caterpillar.heading() == 270:
#         caterpillar.setheading(180)
# def move_right():
#     if caterpillar.heading() == 90 or caterpillar.heading() == 270:
#         caterpillar.setheading(0)
#         t.onkey(start_game, 'space' )
#         t.onkey(move_up, 'Up') 
#         t.onkey(move_right, 'Right')
#         t.onkey(move_down, 'Down')
#         t.onkey(move_left, 'Left')
#         t.listen()



import random
import turtle as t

# Set up game window
t.bgcolor('yellow')

# Caterpillar setup
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# Leaf setup
leaf = t.Turtle()
leaf_shape = ((0,0), (14,2), (18,6), (20,20), (6,18), (2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

# Game state
game_started = False

# Text turtles
text_turtle = t.Turtle()
text_turtle.write('PRESS SPACE TO START', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    """Check if caterpillar is outside the window."""
    left_wall = -t.window_width() / 2 
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    x, y = caterpillar.pos()
    return x < left_wall or x > right_wall or y < bottom_wall or y > top_wall

def game_over():
    """End the game and display 'GAME OVER'."""
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.goto(0, 0)
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    """Update the score display."""
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    """Randomly place the leaf on the screen."""
    leaf.hideturtle()
    leaf.setx(random.randint(-200, 200))  
    leaf.sety(random.randint(-200, 200))
    leaf.showturtle()

def start_game():
    """Start the caterpillar game."""
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    
    # Initialize caterpillar properties
    caterpillar_speed = 2 
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    
    display_score(score)
    place_leaf()
    
    while True:
        caterpillar.forward(caterpillar_speed)
        
        # If caterpillar eats the leaf
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        
        # If caterpillar hits the wall
        if outside_window():
            game_over()
            break

# Movement functions
def move_up():
    if caterpillar.heading() in [0, 180]:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() in [0, 180]:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() in [90, 270]:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() in [90, 270]:
        caterpillar.setheading(0)

# Keyboard bindings
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up') 
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')

t.listen()
t.mainloop()






