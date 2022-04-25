from sqlite3 import DatabaseError
from numpy import uint32
from numpy import int32
from numpy import float32
from numpy import bool8
import serial
from serial.tools import list_ports

class dataString:
    p: float32
    x: float32
    y: float32
    z: float32

    gpslat: uint32
    gpslong: uint32
    altitude: uint32 #cm

    #velocity with respect to vehicle frame
    velocity_X: int32 #mm/s 
    velocity_Y: int32 #mm/s
    velocity_Z: int32 #mm/s

    has_Launched: bool8
    has_Apogee: bool8
    has_Drogue: bool8
    has_Main: bool8
    has_Landed: bool8



def SerialPortList():
    ser = serial.Serial()
    ser.baudrate = 57600
    ser.port = '/dev/ttyUSB0'
    print(list(list_ports.comports()))

