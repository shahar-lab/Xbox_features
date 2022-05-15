# Pygame is a set of Python modules designed for writing video games and adds functionality for
# reading different events from different devices connected to the computer

# Import pygame to use its' modules
import pygame

# Initializing all pygame modules and then Joystick connection in order to use with code
# to read events from joystick and use the pygame module in experiment. 
# This is the first step to be done in order to access other pygame modules. 
pygame.init() #Initialized pygame modules
j = pygame.joystick.Joystick(0) #Pygame module for interacting with joysticks - creates a new Joystick object.
j.init() #initialize the Joystick

# pygame.event is a pygame module for interacting with events and queues
# Getting events: poll() chooses one single event from pending events in defined joystick
# Link to all functions with pygame.event - https://www.pygame.org/docs/ref/event.html
events = pygame.event.poll() #Get a single event from the queue, the returned event is removed from the queue.
pygame.event.get() # This will get all the messages and remove them from the queue.

# Check event type: Can be useful to differentiate between pressing joystick button down/releasing button or moving joystick axis
# example:
events.type == pygame.JOYBUTTONDOWN # Check the type of event that was received in the previous line of code
                                    # This example checks if the event recorded was a button pressed down on the joystick
                                    # Other types examples are JOYAXISMOTION - in case we want to check if event was motion of axis on joystick
                                    # JOYBUTTONUP - events that occur the moment a button is RELEASED up AFTER being pressed down 
                                    # Other event types are included in this link https://www.raspberry-pi-geek.com/Archive/2014/05/Pygame-modules-for-interactive-programs

# [JOYBUTTONDOWN | JOYBUTTONUP ]'s Different button values: 
# Values differ between different joystick brands - these specific value are for the Xbox Controller
# A = 0
# B = 1
# X = 2
# Y = 3
# Left bumper -> LB = 4
# Right bumper -> RB = 5
# BACK = 6
# START = 7
# XBOX = 8
# LEFTTHUMB Stick = 9
# RIGHTTHUMB Stick = 10
if (events.button) == 5: # Here we check if the participant pressed DOWN the right bumper button,
                        # you can replace value 5 with any other value from above. 
                        # This command will be used to determine the next move of the code or game according to
                        # the participants' reaction (Which button was pressed down in this example)
    print("pressed DOWN right bumper button")


