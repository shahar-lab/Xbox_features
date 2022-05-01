import pygame

# Initializing game
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

# Getting events: poll() chooses one single event
# Link to all functions with pygame.event - https://www.pygame.org/docs/ref/event.html

events = pygame.event.poll()

# Check event type: Can be useful to differentiate between pressing joystick button down, or moving joystick axis
# JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONUP, JOYBUTTONDOWN 
# Different types table - https://www.raspberry-pi-geek.com/Archive/2014/05/Pygame-modules-for-interactive-programs
# example:
events.type == pygame.JOYBUTTONDOWN

# JOYBUTTONDOWN | JOYBUTTONUP Different button value: 
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

if (events.button) == 5: 
    print("pressed DOWN/UP right bumper button")


