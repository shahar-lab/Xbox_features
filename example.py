import psychopy
from psychopy import core, visual, gui, data
import pygame, time, ctypes

# What this code does is it waits for a reponse from the participant and then: 
# 1. if the respondant pressed down left trigger button on the xbox controller - left motor is activated for 0.45 seconds
# 2. if the respondant pressed down right trigger button on the xbox controller - right motor is activated for a full second

# Create a window
win = visual.Window(
       [800, 600], fullscr = True, monitor="testMonitor", units="deg", color=(-1, -1, -1), useFBO=False
    )

trials = 10 # number of trials

def main(win):
    
    # Initilizing Game
    pygame.init()
    j = pygame.joystick.Joystick(0)
    j.init()

    for trial in range(1, trials+1):
        while True:
            events = pygame.event.poll()
            if (events.type == pygame.JOYBUTTONDOWN):
                #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                if events.button == 4:
                    # Set vibration in left motor (Intensity is 1 * 65535) for 0.45 seconds then shut off
                    set_vibration(0, 1, 0)
                    time.sleep(0.45)
                    set_vibration(0, 0, 0)
                    break

                elif events.button == 5:     
                    # Set vibration in right motor (intensity is 0.5 * 65535) for 1 second then shut off
                    set_vibration(0, 0, 0.5)
                    time.sleep(1)
                    set_vibration(0, 0, 0)
                    break   

main(win)

#   **  Rumble Feature  **

class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]
xinput = ctypes.windll.xinput1_4  # Load Xinput.dll

# Set up function argument types and return type
XInputSetState = xinput.XInputSetState
XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
XInputSetState.restype = ctypes.c_uint

# A helper function:
def set_vibration(controller, left_motor, right_motor):
    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535))
    XInputSetState(controller, ctypes.byref(vibration))
