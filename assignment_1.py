
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2023.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11537400
student_name   = "Bailey Watts"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('assignment_1_config.py'):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print("\nCannot find file 'assignment_1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('assignment_1_data_source.py'):
    print('Data generation module found ...\n')
    from assignment_1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# Make sure that your code does NOT call function data_set (or
# raw_data) because it's already called in the main program below.
def visualise_data(tank_traverse):
    speed("fastest")
    tracer(0)
    # Define some constants
    hexagonal_side_length = 60
    hull_width = 100 // 3
    hull_height = 150 // 3
    track_width = 40 // 3
    track_height = 200 // 3
    turret_width = 60 // 3
    turret_height = 60 // 3
    barrel_length = 80 // 3
    nozzle_height = 20 // 3
    nozzle_width = 12 // 3
    commander_canopy_size = 10 // 3
    exhaust_height = 10 // 3
    exhaust_width = 15 // 3
    shovel_handle = 75 // 3
    shovel_head = 12 // 3

    # Define Hexagonal Backdrop
    def hexagon(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        backward(hexagonal_side_length // 2)
        left(90)
        forward(51.96)
        right(90)
        pendown()
        fillcolor("alice blue")
        begin_fill()
        for hexagonal_shape in range(6):
            forward(hexagonal_side_length)
            right(60)
        end_fill()
        penup()

    # Define Tank Shapes
    # Define Tank Hull Function
    def tank_hull(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        backward(hull_width // 2)
        left(90)
        forward(hull_height // 2)
        right(90)
        pendown()
        pencolor("black")
        begin_fill()
        fillcolor("olive drab")
        for hull_square in range(2):
            forward(hull_width)
            right(90)
            forward(hull_height)
            right(90)
        end_fill()
        penup()
    # Define Left Tank Track Function
    def tank_track_left(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        backward(hull_width // 2 + track_width)
        left(90)
        forward(hull_height // 2 + 25 // 3)
        right(90)
        pendown()
        pencolor("black")
        begin_fill()
        fillcolor("olive drab")
        for track_left_shape in range(2):
            forward(track_width)
            right(90)
            forward(track_height)
            right(90)
        end_fill()
        penup()
    # Define Right Track Function
    def tank_track_right(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        forward(hull_width // 2)
        left(90)
        forward(hull_height // 2 + 25 // 3)
        right(90)
        pendown()
        pencolor("black")
        begin_fill()
        fillcolor("olive drab")
        for track_right_shape in range(2):
            forward(track_width)
            right(90)
            forward(track_height)
            right(90)
        end_fill()
        penup()
    # Define Tank Turret shape as a function
    def tank_turret(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        backward(turret_width // 2)
        left(90)
        forward(turret_height - 15 // 3)
        right(90)
        pendown()
        pencolor("black")
        begin_fill()
        fillcolor("olive drab")
        for turret_shape in range(2):
            forward(turret_width)
            right(90)
            forward(turret_height)
            right(90)
        end_fill()
        penup()
    # Define Tank Barrel shape as a function
    def tank_barrel(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        left(90)
        forward(turret_height - 15 // 3)
        pendown()
        pencolor("black")
        width(2.5)
        forward(barrel_length)
        width(1)
        penup()
    # Define Tank Barrel Nozzle shape as a function
    def tank_barrel_nozzle(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        backward(nozzle_width // 2)
        left(90)
        forward(turret_height - 15 // 3 + barrel_length)
        pendown()
        pencolor("black")
        begin_fill()
        fillcolor("olive drab")
        for nozzle in range(2):
            forward(nozzle_height)
            right(90)
            forward(nozzle_width)
            right(90)
        end_fill()
        penup()
    # Define Commander Canopy shape as a function
    def commander_canopy(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        forward(10 // 3)
        pendown()
        pencolor("black")
        fillcolor("dark olive green")
        begin_fill()
        circle(commander_canopy_size)
        end_fill()
        penup()
    # Define Exhaust shape as a function
    def exhaust(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        right(90)
        forward(hull_height // 3)
        left(90)
        backward(exhaust_width // 2 + exhaust_width)
        pendown()
        pencolor("black")
        fillcolor("dim gray")
        for multiple_exhausts in range(3):
            begin_fill()
            for exhaust_shape in range(2):
                forward(exhaust_width)
                right(90)
                forward(exhaust_height)
                right(90)
            end_fill()
            forward(exhaust_width)
        backward(exhaust_width * 3)
        left(90)
        forward(exhaust_height)
        right(90)
        for multiple_exhausts in range(3):
            begin_fill()
            for exhaust_shape in range(2):
                forward(exhaust_width)
                right(90)
                forward(exhaust_height)
                right(90)
            end_fill()
            forward(exhaust_width)
        penup()
    # Define Shovel shape as a function
    def shovel(x, y, heading):
        penup()
        goto(x, y)
        setheading(heading)
        forward(hull_width // 2 + track_width // 2)
        left(90)
        backward(shovel_handle // 2)
        pendown()
        pencolor("saddle brown")
        pensize(3)
        forward(shovel_handle)
        pensize(1)
        right(90)
        penup()
        forward(shovel_head)
        left(90)
        pencolor("black")
        fillcolor("dim gray")
        begin_fill()
        circle(shovel_head, 180)
        end_fill()
        goto(x, y)
        left(180)
        penup()

    # Define North Tank position as a function
    def tank_north(x, y):
        hexagon(x, y, 0)
        tank_hull(x, y, 0)
        tank_track_left(x, y, 0)
        tank_track_right(x, y, 0)
        tank_turret(x, y, 0)
        tank_barrel(x, y, 0)
        tank_barrel_nozzle(x, y, 0)
        commander_canopy(x, y, 0)
        exhaust(x, y, 0)
        shovel(x, y, 0)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("North", align = "center", font = "bold")
    # Define North-West Tank position as a function
    def tank_north_west(x, y):
        hexagon(x, y, 60)
        tank_hull(x, y, 60)
        tank_track_left(x, y, 60)
        tank_track_right(x, y, 60)
        tank_turret(x, y, 60)
        tank_barrel(x, y, 60)
        tank_barrel_nozzle(x, y, 60)
        commander_canopy(x, y, 60)
        exhaust(x, y, 60)
        shovel(x, y, 60)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("North-West", align = "center", font = "bold")
    # Define South-West Tank position as a function
    def tank_south_west(x, y):
        hexagon(x, y, 120)
        tank_hull(x, y, 120)
        tank_track_left(x, y, 120)
        tank_track_right(x, y, 120)
        tank_turret(x, y, 120)
        tank_barrel(x, y, 120)
        tank_barrel_nozzle(x, y, 120)
        commander_canopy(x, y, 120)
        exhaust(x, y, 120)
        shovel(x, y, 120)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("South-West", align = "center", font = "bold")
    # Define South Tank position as a function
    def tank_south(x, y):
        hexagon(x, y, 180)
        tank_hull(x, y, 180)
        tank_track_left(x, y, 180)
        tank_track_right(x, y, 180)
        tank_turret(x, y, 180)
        tank_barrel(x, y, 180)
        tank_barrel_nozzle(x, y, 180)
        commander_canopy(x, y, 180)
        exhaust(x, y, 180)
        shovel(x, y, 180)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("South", align = "center", font = "bold")
    # Define South-East Tank position as a function
    def tank_south_east(x, y):
        hexagon(x, y, 240)
        tank_hull(x, y, 240)
        tank_track_left(x, y, 240)
        tank_track_right(x, y, 240)
        tank_turret(x, y, 240)
        tank_barrel(x, y, 240)
        tank_barrel_nozzle(x, y, 240)
        commander_canopy(x, y, 240)
        exhaust(x, y, 240)
        shovel(x, y, 240)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("South-East", align = "center", font = "bold")
    # Define North-East Tank position as a function
    def tank_north_east(x, y):
        hexagon(x, y, 300)
        tank_hull(x, y, 300)
        tank_track_left(x, y, 300)
        tank_track_right(x, y, 300)
        tank_turret(x, y, 300)
        tank_barrel(x, y, 300)
        tank_barrel_nozzle(x, y, 300)
        commander_canopy(x, y, 300)
        exhaust(x, y, 300)
        shovel(x, y, 300)
        goto(x, y)
        setheading(0)
        right(90)
        forward(80)
        left(90)
        write("North-East", align = "center", font = "bold")

    # Draw and position Tanks around canvas
    tank_north(-550, 200)
    tank_north_west(-550, 0)
    tank_south_west(-550, -200)
    tank_south(550, 200)
    tank_south_east(550, 0)
    tank_north_east(550, -200)

    # Define some more useful constraints for directions
    # Note: tanks is draw 90 degrees left from default heading
    north = 0
    north_west = 60
    south_west = 60 * 2
    south = 60 * 3
    south_east = 240
    north_east = 60 * 5
##    current_heading = heading()


    # Define Tank function
    def tank(x, y, heading):
        hexagon(x, y, heading)
        tank_hull(x, y, heading)
        tank_track_left(x, y, heading)
        tank_track_right(x, y, heading)
        tank_turret(x, y, heading)
        tank_barrel(x, y, heading)
        tank_barrel_nozzle(x, y, heading)
        commander_canopy(x, y, heading)
        exhaust(x, y, heading)
        shovel(x, y, heading)
        goto(x, y)

    tracer(0)

    # Draw tank in its initial direction
    initial_direction = tank_traverse[0][2]
    energy = tank_traverse[0][1]
    if initial_direction == 'South east':
        tank(0, 0, south_east)
    elif initial_direction == 'North':
        tank(0, 0, north)
    elif initial_direction == 'North west':
        tank(0, 0, north_west)
    elif initial_direction == 'South west':
        tank(0, 0, south_west)
    elif initial_direction == 'South':
        tank(0, 0, south)
    elif initial_direction == 'South east':
        tank(0, 0, south_east)
    elif initial_direction == 'North east':
        tank(0, 0, north_east)

    # North = heading(0) + left(90)
    # North-West = heading(60) + left(90)
    # South-West = heading(120) + left(90)
    # South = heading(180) + left(90)
    # South-East = heading(240) + left(90)
    # North-East = heading(300) + left(90) = 360 + 30

    # Special cell locations are as follows:
    # H6 is located at 270.00000000000057 51.9615242270674
    # D8 is located at -90.00000000000084 155.8845726811991
    # A3 is located at -360.000000000001 -103.9230484541331

    # Create a for loop for each item in tank_traverse
    for item in tank_traverse:
        move_no = item[0]
        if len(item) == 3:
            if item[1] == 0:
                goto(0, 2 * vert_spacing * (grid_height / 3.1))
                write("The tank ran out of fuel on move " + str(energy), align = 'center', font = label_font)
                break
        if len(item) == 2:
            if move_no <= int(energy):
                if item[1] == 'Move & turn left': # Move & turn left
                    forward(60*sqrt(3))
                    left(-30) # This is because Tank is drawn 90 degrees left of starting heading
                    current_heading = heading()
                    if xcor() >= 450 or xcor() <= -450 or ycor() >= 259 or ycor() <= -255: # If the tank leaves the grid
                        goto(0, 2 * vert_spacing * (grid_height / 3.1))
                        write("The tank deserted the battlefield on move " + str(move_no), align = 'center', font = label_font)
                        break
                    elif xcor() > -450 and xcor() < 450 and ycor() > -255 and ycor() < 259:
                        tank(xcor(), ycor(), current_heading)
                elif item[1] == 'Move forward': # Move forward
                    forward(60*sqrt(3))
                    left(-90)# This is because Tank is drawn 90 degrees left of starting heading
                    current_heading = heading()
                    if xcor() >= 450 or xcor() <= -450 or ycor() >= 259 or ycor() <= -255: # If the tank leaves the grid
                        goto(0, 2 * vert_spacing * (grid_height / 3.1))
                        write("The tank deserted the battlefield on move " + str(move_no), align = 'center', font = label_font)
                        break
                    elif xcor() > -450 and xcor() < 450 and ycor() > -255 and ycor() < 259:
                        tank(xcor(), ycor(), current_heading)
                elif item[1] == 'Move & turn right': # Move & turn Right
                    forward(60*sqrt(3))
                    left(-150) # This is because Tank is drawn 90 degrees left of starting heading
                    current_heading = heading()
                    if xcor() >= 450 or xcor() <= -450 or ycor() >= 259 or ycor() <= -255: # If the tank leaves the grid
                        goto(0, 2 * vert_spacing * (grid_height / 3.1))
                        write("The tank deserted the battlefield on move " + str(move_no), align = 'center', font = label_font)
                        break
                    elif xcor() > -450 and xcor() < 450 and ycor() > -255 and ycor() < 259:
                        tank(xcor(), ycor(), current_heading)
                if abs(xcor() - 270.00000000000057) < 0.0001 and abs(ycor() - 51.9615242270674) < 0.0001: # If tank arrives at H6, break loop
                    goto(0, 2 * vert_spacing * (grid_height / 3.1))
                    write("The tank arrived at its destination at cell H6", align = 'center', font = label_font)
                    break
                if xcor() == -90.00000000000084 and ycor() == 155.8845726811991: # If tank arrives at D8, break loop
                    goto(0, 2 * vert_spacing * (grid_height / 3.1))
                    write("The tank arrived at its destination at cell D8", align = 'center', font = label_font)
                    break
                if abs(xcor() - (-360.000000000001)) < 0.0001 and abs(ycor() - (-103.9230484541331)) < 0.0001: # If tank arrives at A3, break loop
                    goto(0, 2 * vert_spacing * (grid_height / 3.1))
                    write("The tank arrived at its destination at cell A3", align = 'center', font = label_font)
                    break
                if move_no == int(energy):
                    goto(0, 2 * vert_spacing * (grid_height / 3.1))
                    write("The tank ran out of moves on move " + str(move_no), align = 'center', font = label_font)
                    break
            elif move_no > energy:
                goto(0, 2 * vert_spacing * (grid_height / 3.1))
                write("The tank ran out of fuel after move " + str(energy), align = 'center', font = label_font)
                break




#
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(canvas_title = "Tanks, Roll Out!", write_instructions = False)

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
