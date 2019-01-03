import PIL.ImageGrab
from win32api import GetSystemMetrics
import socket
import pickle  # Module for turning an instance to a string and the opposite
PORT_NUMBER = 8820
BUFFER_SIZE = 1024

#my_socket = socket.socket()
#my_socket.connect(('127.0.0.1', PORT_NUMBER))

WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))


list_pixels = []
im = PIL.ImageGrab.grab()
im.save("C:\\Users\\AMIT\\PycharmProjects\\project\\image.jpg", )
pixel = im.load()
for x in range(WIDTH):
    for y in range(HEIGHT):
       list_pixels.append(pixel[x, y])  # Get the RGB Value of the a pixel of an image
im2 =
# print (list_pixels)
list_pixels_for_server = pickle.dumps(list_pixels)
# print(list_pixels_for_server)
#my_socket.send(list_pixels_for_server)

