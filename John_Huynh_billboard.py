
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 9154566
#    Student name: John Huynh
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

# Paste the sheets onto the billboard as per the provided data set
def paste_up(dummy_parameter):
	graffiti = dummy_parameter[0]
	numberOfSheets = len(dummy_parameter)-1
	
	#Initalise list variables
	sheet = []
	Orientation = []
	Location = []
	
	#Define Sheet/Location/Orientation Index
	Sheet_Index = 0;
	Location_Index = 1;
	Orientation_Index = 2;
	
	#Places sheet/Location/Orientation in their respective list.
	for sheetnumber in range (1,numberOfSheets+1):
		sheet.append(dummy_parameter[sheetnumber][Sheet_Index])
		Location.append(dummy_parameter[sheetnumber][Location_Index])
		Orientation.append(dummy_parameter[sheetnumber][Orientation_Index])
		
	#Determines which sheets to draw and where to draw the sheets
	for sheetnumber in range (0,numberOfSheets):
		#Determines whether Sheet A needs to be drawn
		if(sheet[sheetnumber] == 'Sheet A'):
			Sheet_A(Location[sheetnumber],Orientation[sheetnumber])
		#Determines whether Sheet B needs to be drawn
		elif(sheet[sheetnumber] == 'Sheet B'):
			Sheet_B(Location[sheetnumber],Orientation[sheetnumber])
		#Determines whether Sheet C needs to be drawn
		elif(sheet[sheetnumber] == 'Sheet C'):
			Sheet_C(Location[sheetnumber],Orientation[sheetnumber])
		#Determines whether Sheet D needs to be drawn
		elif(sheet[sheetnumber] == 'Sheet D'):
			Sheet_D(Location[sheetnumber],Orientation[sheetnumber])
	
	#Determines whether graffiti needs to be drawn
	if(graffiti == 'X'):
		draw_Graffito()

#Function that handles drawing Sheet A
def Sheet_A(Location, Orientation):
	#Draws Backround
	DrawBackround(Location,'#013571')
	
	#Choose pen size and colour
	pencolor('white')
	pensize(10)
	
	#Determines the starting location
	x = Determine_starting_Location(Location,Orientation)
	
	#Determine rotation angle and fliping factors
	horizontal_flip_factor = Determine_rotation_fliping_factors(Orientation)[0]
	vertical_flip_factor = Determine_rotation_fliping_factors(Orientation)[1]
	rotation_angle = Determine_rotation_fliping_factors(Orientation)[2]
	
	#Intialise offsets,location variables and radius of circles 
	y_start_of_outside_circle = 150
	x_end_of_line = 43.08
	y_end_of_line = -54.507
	y_end_of_circle= -54.51
	y_end_of_inside_circle = 19;
	x_start_of_triganle= 103.08
	line_offset = 157
	bigCircle_offset = 200
	bigCircle_radius = 130
	insideCircle_radius = 300
	
	
	#Draws a Quater Circle
	goto(x+(vertical_flip_factor*bigCircle_offset),horizontal_flip_factor * y_start_of_outside_circle)
	pendown()
	seth(150 + rotation_angle)
	fillcolor('#FF173E')
	begin_fill()
	circle(bigCircle_radius,165)
	seth(370+rotation_angle)
	
	#Draws the Inner circle
	circle(insideCircle_radius,35)
	end_fill()
	seth(225+rotation_angle)
	fillcolor('white')
	circle(-insideCircle_radius,35)

	#Fill in the middle section
	penup()
	pensize(5)
	goto(x+(vertical_flip_factor*x_start_of_triganle),horizontal_flip_factor * (12+y_end_of_line))
	begin_fill()
	pendown()
	goto(x+(vertical_flip_factor*(x_end_of_line+line_offset)), horizontal_flip_factor * (y_end_of_line+20))
	goto(x+(vertical_flip_factor*bigCircle_offset),horizontal_flip_factor * y_end_of_inside_circle)
	end_fill()
	penup()
	
	
	#Draws the Remainding quater circle
	pensize(10)
	goto(x+(vertical_flip_factor*x_end_of_line),horizontal_flip_factor * y_end_of_circle)
	pendown()
	seth(310+rotation_angle)
	pencolor('white')
	fillcolor('#0177DB')
	begin_fill()
	circle(bigCircle_radius,76)
	
	#Draws the line and fills it
	penup()
	goto(x+(vertical_flip_factor*(x_end_of_line+line_offset)),horizontal_flip_factor * (y_end_of_line+20))
	pendown()
	goto(x+(vertical_flip_factor*x_end_of_line),horizontal_flip_factor * y_end_of_line)
	end_fill()
	penup()
	

#Function that handles drawing sheet B
def Sheet_B(Location, Orientation):
	DrawBackround(Location,'#013571')
	
	#Chooses pen size and colour
	pencolor('white')
	pensize(10)

	#Determines the starting location
	x = Determine_starting_Location(Location,Orientation)
	
	#Determine rotation angle and fliping factors
	horizontal_flip_factor = Determine_rotation_fliping_factors(Orientation)[0]
	vertical_flip_factor = Determine_rotation_fliping_factors(Orientation)[1]
	rotation_angle = Determine_rotation_fliping_factors(Orientation)[2]
	
	#Intialise offsets,location variables and radius of circles
	x_end_of_start_circle = 64.03
	y_end_of_start_circle = 40.43
	y_start_of_outside_circle = -88
	y_end_of_inside_circle = -36.69
	P_offset = 160
	P_line_start = -100
	P_line_end = 20
	P_circle_offset = 200
	P_circle_radius = 40
	P_circle_y_start = 40
	bigCircle_radius = 130
	insideCircle_radius = 300
	insideSmallCircle_radius = 100
	
	#Draws the a quater circle 
	goto(x,horizontal_flip_factor * y_start_of_outside_circle)
	pendown()
	seth(30 + rotation_angle)
	fillcolor('#0177DB')
	begin_fill()
	circle(bigCircle_radius,66)
	
	#Draws the Inner Circle at the base of the circle
	seth(260 + rotation_angle)
	circle(-insideSmallCircle_radius,60)
	end_fill()
	penup()
	
	#Fills in the middle section
	goto(x,horizontal_flip_factor * y_end_of_inside_circle)
	fillcolor('white')
	begin_fill()
	pendown()
	seth(380 + rotation_angle)
	circle(insideSmallCircle_radius,60)
	
	#draws a 1/10 of a circle to fill in the middle section
	goto(x+(vertical_flip_factor * x_end_of_start_circle),horizontal_flip_factor * y_end_of_start_circle)
	pendown()
	seth(100 + rotation_angle)
	circle(bigCircle_radius,20)
	seth(223 + rotation_angle)
	circle(insideCircle_radius,15)
	end_fill()
	
	#Draws the Inner Circle at the top of the cicle and fills it
	seth(57 + rotation_angle)
	fillcolor('#FF173E')
	begin_fill()
	circle(-insideCircle_radius,15)
	seth(107 + rotation_angle)
	
	#Finish drawing the remainder of the otherside circle
	circle(bigCircle_radius,39)
	end_fill()
	penup()
	
	#letter P
	#Draws the line for P
	goto(x + (vertical_flip_factor * P_offset),horizontal_flip_factor * P_line_start)
	pendown()
	goto(x + (vertical_flip_factor * P_offset),horizontal_flip_factor * P_line_end)
	penup()
	#Draws the Circle for P
	goto(x + (vertical_flip_factor * P_circle_offset),horizontal_flip_factor * P_circle_y_start)
	pendown()
	seth(180 + rotation_angle)
	circle(P_circle_radius,180)
	penup()
	
#Function that handles drawing sheet C
def Sheet_C(Location, Orientation):
	DrawBackround(Location,'#013571')
	
	#Choose pen size and colour
	pencolor('white')
	pensize(10)

	#Determines the starting location
	x = Determine_starting_Location(Location,Orientation)
	
	#Determine rotation angle and fliping factors
	horizontal_flip_factor = Determine_rotation_fliping_factors(Orientation)[0]
	vertical_flip_factor = Determine_rotation_fliping_factors(Orientation)[1]
	rotation_angle = Determine_rotation_fliping_factors(Orientation)[2]
		
	#Intialise offsets, location variables and radius of circles
	E_offset = 150
	E_circle_y_start = 5
	E_line = 78
	E_circle_radius = 40
	P_offset = 180
	P_circle_radius = 40
	P_circle_offset = 200
	P_circle_y_start = 30
	P_circle_y_end = -40
	P_line_start = -100
	P_line_end = 20

	#Finish off Letter P
	goto(x,horizontal_flip_factor * P_circle_y_end)
	pendown()
	seth(0+rotation_angle)
	circle(P_circle_radius,180)
	penup()
	
	#letter E
	#Draw outside circle for E
	goto(x+(vertical_flip_factor * E_offset),E_circle_y_start)
	pendown()
	seth(100+rotation_angle)
	circle(E_circle_radius,320)
	penup()
	#Draw the line to finsh E
	goto(x+(vertical_flip_factor * E_offset),E_circle_y_start)
	pendown()
	goto(x+(vertical_flip_factor * E_line),E_circle_y_start)
	penup()

	#Start of Letter P
	#Draws the line for P
	goto(x + (vertical_flip_factor * P_offset), horizontal_flip_factor * P_line_start)
	pendown()
	goto(x + (vertical_flip_factor * P_offset), horizontal_flip_factor * P_line_end)
	penup()
	#Draws the circle for P
	goto(x + (vertical_flip_factor * P_circle_offset), horizontal_flip_factor * P_circle_y_start)
	pendown()
	seth(210 + rotation_angle)
	circle(P_circle_radius,120)
	penup()


#Function that handles drawing sheet D
def Sheet_D(Location,Orientation):
	DrawBackround(Location,'#013571')
	
	#Choose pen size and colour
	pencolor('white')
	pensize(10)

	#Determines the starting location 
	x = Determine_starting_Location(Location,Orientation)
	
	point_size = 10;
	
	#determine flipping factors and rotation angles based on Orientation
	horizontal_flip_factor = Determine_rotation_fliping_factors(Orientation)[0]
	vertical_flip_factor = Determine_rotation_fliping_factors(Orientation)[1]
	rotation_angle = Determine_rotation_fliping_factors(Orientation)[2]
	
	#Intialise offsets, location variables and radius of circles
	i_offset = 175;
	i_line_start = -50
	i_line_end = 25
	i_dot = 45
	s_start_x = 90
	s_start_y = -40
	s_middle_x = 105
	s_middle_y = -43
	s_middle_end_y = -6;
	s_end_section_start_x = 120
	s_end_section_start_y = 25
	s_end_setction_end_x = 127
	s_end_section_end_y = 23
	s_circle_radius = 17
	P_circle_radius = 40
	
	#finish off P
	#Draw the remainder of the circle for P
	goto(x,horizontal_flip_factor * -40)
	pendown()
	seth(330 + rotation_angle)
	circle(P_circle_radius,240)
	penup()
	seth(0)
	
	#Letter S
	#Draw the bottom line for s
	goto(x + (vertical_flip_factor * s_start_x),horizontal_flip_factor * s_start_y)
	pendown()
	goto(x + (vertical_flip_factor * s_middle_x),horizontal_flip_factor * s_middle_y)
	
	#draw circle connected to middle of S
	seth(340 + rotation_angle)
	circle(s_circle_radius,180)
	goto(x + (vertical_flip_factor * s_middle_x),horizontal_flip_factor * s_middle_end_y)
	#Draw another cirlce but opposite direction connected to top of S
	circle(-s_circle_radius,180)
	#Draw line at the top to finish S
	goto(x + (vertical_flip_factor * s_end_section_start_x),horizontal_flip_factor * s_end_section_start_y)
	goto(x + (vertical_flip_factor * s_end_setction_end_x) ,horizontal_flip_factor * s_end_section_end_y)
	penup()
	
	#Letter I
	#Draw Line for I
	goto(x + (vertical_flip_factor * i_offset),horizontal_flip_factor * i_line_start)
	pendown()
	goto(x + (vertical_flip_factor * i_offset),horizontal_flip_factor * i_line_end)
	penup()
	#Draw dot for I
	goto(x + (vertical_flip_factor * i_offset),horizontal_flip_factor * i_dot)
	dot(point_size)
	penup()
	
#Function that handles drawing the Graffiti
def draw_Graffito():

	#Intialise cordinate varables
	J_top_start_x = -300
	J_top_end_x = -100
	J_top_y = 150
	J_top_middle = -200
	J_line_y = -100
	J_circle_radius = -80
	Dot_x = 0
	Dot_y = -150
	Dot_radius = 40
	H_left_line_x = 100;
	H_left_line_start_y = 150
	H_left_line_end_y = -150
	H_middle_line_x = 100
	H_middle_y = 0
	H_middle_end_x = 300
	H_right_line_x = 300
	H_right_line_start_y = 150 
	H_right_line_end_y = -150
	
	#Define pen colour and size
	pensize(20)
	pencolor('black')
	
	#Draw J
	#Draw top section of J
	goto(J_top_start_x,J_top_y)
	pendown()
	goto(J_top_end_x,J_top_y)
	penup()
	#Draw Lower Section of J
	goto(J_top_middle,J_top_y)
	pendown()
	goto(J_top_middle,J_line_y)
	seth(270)
	circle(J_circle_radius,180)
	
	#Draw Full Stop
	penup()
	goto(Dot_x,Dot_y)
	dot(Dot_radius)
	
	#Draw H	
	#Draw Line for left side for H
	goto (H_left_line_x,H_left_line_start_y)
	pendown()
	goto(H_left_line_x ,H_left_line_end_y)
	penup()
	#Draw middle line connecting left side to right side for H
	goto(H_middle_line_x,H_middle_y)
	pendown()
	goto(H_middle_end_x,H_middle_y)
	penup()
	#Draw line for right side of H
	goto(H_right_line_x,H_right_line_start_y)
	pendown()
	goto(H_right_line_x,H_right_line_end_y)
	penup()
	
#Function that deals with drawing backround
def DrawBackround(Location, colour):
	#Determine starting postion
	y = -250
	if (Location == "Location 1"):
		x = -400
	elif(Location == "Location 2"):
		x = -200
	elif(Location == "Location 3"):
		x = 0
	elif(Location == "Location 4"):
		x = 200
	
	penup()
	pencolor(colour)
	goto(x,y)
	fillcolor(colour)
	begin_fill()
	goto(x+200,y)
	goto(x+200,y+500)
	goto(x,y+500)
	end_fill()
	penup()

#Function that determines the starting location and returns the value
def Determine_starting_Location(Location,Orientation):
	#Determines the starting x cordinate depending based on location
	if (Location == "Location 1"):
		if(Orientation == "Upright"):
			return -400
		else:
			return -200
	elif(Location == "Location 2"):
		if(Orientation == "Upright"):
			return -200
		else:
			return 0
	elif(Location == "Location 3"):
		if(Orientation == "Upright"):
			return 0
		else:
			return 200
	elif(Location == "Location 4"):
		if(Orientation == "Upright"):
			return 200
		else:
			return 400
	
#Function that determines the rotation/flipping factors
def Determine_rotation_fliping_factors(Orientation):
	flip_factor = []
	#determine Flipping factors and rotation angles based on Orientation
	if (Orientation == 'Upright'):
		horizontal_flip_factor = 1
		vertical_flip_factor = 1
		rotation_angle = 0	
	else:
		horizontal_flip_factor = -1
		vertical_flip_factor = -1
		rotation_angle = 180
	#Stores flip and rotation factors in a list
	flip_factor.extend([horizontal_flip_factor,vertical_flip_factor,rotation_angle])
	return flip_factor

#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('normal')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Pepsi Logo")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set

paste_up(data_sets[51])

#Upright
# paste_up(data_sets[2])
# paste_up(data_sets[11])
# paste_up(data_sets[20])
# paste_up(data_sets[29])

#Upside Down
# paste_up(data_sets[6])
# paste_up(data_sets[15])
# paste_up(data_sets[24])
# paste_up(data_sets[33])

#Upside down correct order
# paste_up(data_sets[9])
# paste_up(data_sets[16])
# paste_up(data_sets[23])
# paste_up(data_sets[30])

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

