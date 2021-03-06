#Pong
#Aadil Islam
#January 30, 2018

from cs1lib import *
from random import *

#constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#more constants, adjust as you please!
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_MOVEMENT = 7
BALL_SIZE = 20

#initial left/right paddle coordinates
l_x = 0
l_y = 0
r_x = WINDOW_WIDTH - PADDLE_WIDTH
r_y = WINDOW_HEIGHT - PADDLE_HEIGHT

#initial ball coordinates
b_x = WINDOW_WIDTH/2
b_y = WINDOW_HEIGHT/2

#track state of directional keys
is_a_pressed = False
is_z_pressed = False
is_k_pressed = False
is_m_pressed = False

#initialize ball direction
horiz_move = 5
vert_move = 4

#reset game
send_ball_to_center = False

#identify a pressed key
def keypress(key):

    global is_a_pressed, is_z_pressed, is_k_pressed, is_m_pressed, send_ball_to_center

    if key == 'a':
        is_a_pressed = True
    elif key == 'z':
        is_z_pressed = True
    elif key == 'k':
        is_k_pressed = True
    elif key == 'm':
        is_m_pressed = True
    elif key == 'q':
        #time to exit game
        cs1_quit()
    elif key == ' ':
        #time to reset game
        send_ball_to_center = True
    else:
        print("Invalid input, try again.")

#identify when user lets go of key, or else paddle just keeps moving!
def keyrelease(key):

    global is_a_pressed, is_z_pressed, is_k_pressed, is_m_pressed

    if key == 'a':
        is_a_pressed = False
    elif key == 'z':
        is_z_pressed = False
    elif key == 'k':
        is_k_pressed = False
    elif key == 'm':
        is_m_pressed = False

#true when ball is too close to right wall
def right_wall_collision():

    if b_x > WINDOW_WIDTH - BALL_SIZE:
        return True
    else:
        return False

#true when ball is too close to left wall
def left_wall_collision():

    if b_x - BALL_SIZE < 0:
        return True
    else:
        return False

#true ball hits anywhere on right paddle
def right_pad_collision():

    if (b_x + BALL_SIZE >= r_x) and (b_y + BALL_SIZE > r_y) and (b_y - BALL_SIZE < r_y + PADDLE_HEIGHT):
        return True
    else:
        return False

#true ball hits anywhere on left paddle
def left_pad_collision():

    if ((b_x - BALL_SIZE <= l_x + PADDLE_WIDTH)) and (b_y + BALL_SIZE > l_y) and (b_y - BALL_SIZE < l_y + PADDLE_HEIGHT):
        return True
    else:
        return False

#true when ball needs to bounce off of upper/lower wall
def side_wall_collisions():

    if (b_y - BALL_SIZE < 0) or (b_y + BALL_SIZE > WINDOW_HEIGHT):
        return True
    else:
        return False

#how ball behaves in pong
def move_ball():

    global b_x, b_y, first_touch, horiz_move, vert_move

    #if ball needs to bounce off a paddle
    if right_pad_collision() or left_pad_collision():

        #flip direction it was originally moving
        horiz_move = -horiz_move

    #if ball hits upper/lower wall, horizontal mvmt stays same, only vertical mvmt flips
    if side_wall_collisions():
        vert_move = -vert_move

    #keep moving the ball
    b_x += horiz_move
    b_y += vert_move

def graphics():

    global l_x,l_y,r_x,r_y,b_x,b_y,horiz_move,vert_move,send_ball_to_center

    #create black background
    set_clear_color(0,0,0)
    clear()

    #draw ball
    set_fill_color(1,1,0)
    draw_circle(b_x,b_y,BALL_SIZE)

    #draw red paddles
    set_fill_color(1, 0, 0)
    draw_rectangle(l_x, l_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(r_x, r_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    #if game needs to reset
    if right_wall_collision() or left_wall_collision() or send_ball_to_center:

        #move paddles back to original spots
        l_x = 0
        l_y = 0
        r_x = WINDOW_WIDTH - PADDLE_WIDTH
        r_y = WINDOW_HEIGHT - PADDLE_HEIGHT

        #move ball back to center
        b_x = WINDOW_WIDTH / 2
        b_y = WINDOW_HEIGHT / 2

        #initialize ball direction again
        horiz_move = 5
        vert_move = 4

        #no longer in reset mode
        send_ball_to_center = False

    move_ball()

    # if this key is pressed...
    if is_a_pressed:

        # ...check if paddle is too close to top of window...
        if l_y >= PADDLE_MOVEMENT:
            # ...if not too close, move up
            l_y -= PADDLE_MOVEMENT

    if is_z_pressed:

        # ...check if paddle is too close to bottom of window...
        if (l_y + PADDLE_HEIGHT + PADDLE_MOVEMENT <= WINDOW_HEIGHT):
            # ...if not too close, move down
            l_y += PADDLE_MOVEMENT

    if is_k_pressed:

        # ...check if paddle is too close to top of window...
        if r_y >= PADDLE_MOVEMENT:
            # ...if not too close, move up
            r_y -= PADDLE_MOVEMENT

    if is_m_pressed:

        # ...check if paddle is too close to bottom of window...
        if (r_y + PADDLE_HEIGHT + PADDLE_MOVEMENT <= WINDOW_HEIGHT):
            # ...if not too close, move down
            r_y += PADDLE_MOVEMENT

start_graphics(graphics, 2400, key_press=keypress, key_release=keyrelease)