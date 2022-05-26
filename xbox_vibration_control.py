import ctypes

# Rumble Feature

# In order to initiate a rumble effect in C, we'd use a XInputSetState() function to control the rumble.
# We can access that from Python using the ctypes library and example codes provided in ctypes lib documentation 
# Define necessary structures with controller motors 
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]

xinput = ctypes.windll.xinput1_4  # Load Xinput.dll

# Set up function argument types and return type
XInputSetState = xinput.XInputSetState
XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
XInputSetState.restype = ctypes.c_uint

# A helper function which can be used as is to set the desired vibration conditions
def set_vibration(controller, left_motor, right_motor): # In the case that only one controller is connected - "controller" = 0
    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535)) #Numbers could be changed depending on the desired rumble intensity - 65535 is 100% of the motor. [Not sure how or why these are the values but it's in the documentation I found in the original code]
    XInputSetState(controller, ctypes.byref(vibration))
