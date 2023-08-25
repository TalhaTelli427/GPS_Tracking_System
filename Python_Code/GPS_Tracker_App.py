import serial
from tkinter import *
import tkintermapview
SerialObj_kontrol = serial.Serial('COM16')
SerialObj_kontrol.baudrate = 115200  # set Baud rate to 9600
SerialObj_kontrol.bytesize = 8  # Number of data bits = 8
SerialObj_kontrol.parity = 'N'  # No parity
SerialObj_kontrol.stopbits = 1  # Number of Stop bits = 1
latitude = 0.0
longitude = 0.0
last_longitude=0.0
last_latitude=0.0
root=Tk()
root.title('GPS Tracker')
root.geometry("1280x720")
my_label=LabelFrame(root)
my_label.pack(pady=20)
map_widget=tkintermapview.TkinterMapView(my_label,width=1100,height=900)
map_widget.pack()

def update_map():
    try:
        global latitude, longitude,last_latitude,last_longitude

        mainmpudata = SerialObj_kontrol.readline().decode("utf-8")
        if (mainmpudata[0:2] == "LA"):
            latitude = float(mainmpudata[2:11])

            print(latitude)
        elif (mainmpudata[0:2] == "LO"):
            longitude = float(mainmpudata[2:11])
            print(longitude)
        if(longitude!=last_latitude or latitude!=last_latitude):
            map_widget.delete_all_marker()

        map_widget.set_position(latitude, longitude, marker=True)
        last_latitude = latitude
        last_longitude = longitude

        root.after(100, update_map)

    except:
        root.after(100, update_map)

update_map()
root.mainloop()