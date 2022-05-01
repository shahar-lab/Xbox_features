import ctypes

# Rumble Feature

# Define necessary structures with controller motors #I need more explanation about what's going here...
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]
xinput = ctypes.windll.xinput1_4  # Load Xinput.dll

# Set up function argument types and return type #where do I put these in my code?
XInputSetState = xinput.XInputSetState
XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
XInputSetState.restype = ctypes.c_uint

# A helper function which can be used as is to set the desired vibration conditions
def set_vibration(controller, left_motor, right_motor): #what is controller?
    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535)) #what are those numbers? 
    XInputSetState(controller, ctypes.byref(vibration))
