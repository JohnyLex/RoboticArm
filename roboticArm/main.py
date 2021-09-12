"""
Before test and run this program you must install al requaired module
###########################Please insert this comand in your command line##########################
////////////////////////////MODULE FOR GUI/////////////////////////////////////////////////////////
1-pip install inspect-it
2-pip install time
3-pip install functools
4-pip install tkinter
5-pip install cv2
6-pip install PIL.Image, PIL.ImageTk
7-pip install time 
9-pip install serial
10-pip install numpy
11-pip install requests
12-pip install inspect
###################################################################################################
 """
#-------------------Module for GUI-----------------------------------------
from tkinter import *  
from tkinter import ttk 
import time
from functools import partial

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time 
import inspect
import requests
import numpy as np
import serial
"""
Before test and run this program you must install al requaired module
###########################Please insert this comand in your command line##########################
////////////////////////////MODULE FOR MICROSOFT COGNITIVE SERVICE/////////////////////////////////
1-pip install inspect-it

###################################################################################################
 """
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
""" ################################################################################################ """
"""############################################################################################################################ """
"""-----ALGORITM TO DETECT AND CALCULATE TRAJECTORY BETWEEN TERMINAL POINT AND LETTER----"""
"""----IMPORT MODULE BLOCK-----------"""
"""############################################################################################################################ """
import numpy as np
from numpy.linalg import inv

from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense, Activation, BatchNormalization
from keras.models import Sequential
from keras import regularizers
from glob import glob
import cv2
import pandas as pd
global x_diff,y_diff,worldPt_cir,x,y,w,h,cx,cy
from collections import namedtuple
from itertools import groupby
global distance
distance = 0
"""############################################################################################################################ """
"""--------------------------------------Define all variable and constant----------------------------------------- """
global text_rec
global ii,y_diff,x_diff,not_detected_letter,not_detected_letter_pos_dictionary,orderet_lt_dict,detectet_letter,pos_letter_list,pos_dict,centroid_dict,x,y,w,h,cx,cy
text_rec = " "
x_diff = 0
y_diff = 0
ii = 0
type_letter =  False 
input_shape = (30,30,1)
num_classes = 61

""" -----------------------------------------------------------------"""
vide_source = 1
detect_camera_video_source = 0
""" -----------------------------------------------------------------"""
x,y,w,h,cx,cy = 0,0,0,0,0,0
centroid_dict = {}
pos_dict = {}
global pos_letter_list
pos_letter_list= [(0,0,0,0,0)]
global se
se = 0
detectet_letter = ["1"]
orderet_lt_dict ={}
not_detected_letter =["1"]
not_detected_letter_pos_dictionary ={}
#////////////////////////////////////////
### Inputs ---------------------------------------------------------------------------------------
symbols = ['~','`','!','@','#','$','%','^','&','(',')','_','-','=','+',']','}','[','{',';']
numbers = ['0','1','2','3','4','5','6','7','8','9']
small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
### Obtain letter locations -----------------------------------------------------------------------
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K', \
                   'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char_names =capital_letters + small_letters + numbers + symbols
sosedi = {
    "Q":("  ","W"),
    "A":("  ","S"),
    "Z":("  ","X"),
    "W":("Q","E"),
    "S":("A","D"),
    "X":("Z","C"),
    "E":("W","R"),
    "D":("S","F"),
    "C":("X","V"),
    "F":("D","G"),
    "D":("S","F"),
    "V":("C","B"),
    "T":("R","Y"),
    "G":("F","H"),
    "B":("V","N"),
    "Y":("T","U"),
    "H":("G","J"),
    "N":("B","M"),
    "J":("H","K"),
    "M":("N","  "),
    "I":("U","O"),
    "K":("J","L"),
    "O":("I","P"),
    "P":("O","  "),
    "L":("K","  "),
    "R":("E","T"),
    "U":("Y","I")
}
drawing_letter = namedtuple("drawing_letter","letter left_letter right_letter")
drawing_letter_pos =[drawing_letter(" ",(" ",1,1,1,1),(" ",2,2,2,2))]
model_weight_path = 'good1.hdf5'
drawing_letter = namedtuple("drawing_letter","letter Left_Letter lt_lt_pos  Rght_letter rt_lt_pos")
drawing_letter_pos =[drawing_letter("Victor","s",22,"sda",1997)]
# For "Obtain letter locations" section
k = np.array([[628.66, 0.0,    312.45],
              [0.0,    629.83, 247.39],
              [0.0,    0.0,     1.0    ]])
k_inv = inv(k)
depth_cam2key = 253 #millimeter
depth_cam2cir = 202 #millimeter
depth_cir2key = 51
good_inRange_count = 1
global inRange_count
inRange_count = 0
can_publish = False
image_good = False
printed_text =" "
### (end) Inputs ---------------------------------------------------------------------------------------
"""--------------------------------------END-Define all variable and constant----------------------------------------- """
"""############################################################################################################################ """
print(":->OK.")
print(":->Init Convolutional Neuronal Network...")
### Trained Model ---------------------------------------------------------------------------------
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=input_shape))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Flatten())
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.load_weights(model_weight_path)
### (end) Trained Model ---------------------------------------------------------------------------
"""--------------------------------------(end) Trained Model NEURONAL NETWORK INITIALIZE----------------------------------------- """


"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ """
color_label ='yellow'
send_1 ="G90 G21"
detection_mode = 1   #1-Handrwritten , 2=Object recogniton, by default ,user can change by radiobuttons/PS:NO IMPLEMENTED 
color_label ='yellow'
send_1 ="G90 G21"

""" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ """
letter = "Z"
x=-4
y=-13
z=26
idle = "G21G91G1X"+str(x)+"Y"+str(y)+"Z-"+str(z)+"F5000"
idle_back = "G21G91G1X"+str(-x)+"Y"+str(-y)+"Z"+str(z)+"F5000"
ctr = (-12.3,-20.7,-25.5)
entr = (14,-22,-23)
esc = (-9.7,-23.6,-22)
calc = (11.7,-24,-18)
pos_leter = {
    "B": (-5.1,-15.5,-25.5),
    "N": (-3.9,-15.5,-26),
    "M": (-2.8,-15,-27),
    "Z": (-9.9,-16.9,-24),
    "X": (-8.9,-16.4,-24.4),
    "V": (-6.5,-15.9,-25.5),
    "A": (-10,-17.4,-22.5),
    "S": (-9,-17.4,-23.5),
    "D": (-8,-16.9,-24),
    "F": (-7,-16.4,-24.5),
    "G": (-6,-15.9,-24.5),
    "H": (-4.5,-15.9,-25.0),
    "J": (-3,-16.2,-24.9),
    "K": (-1.8,-16.1,-25.3),
    "L": (-0.5,-16.2,-25.3),
    "O": (-1,-16.4,-24),
    "P": (0.5,-16.4,-24),
    "I": (-2,-16.4,-24),
    "U": (-3,-16.4,-23.5),
    "Y": (-4.4,-16.8,-23.5),
    "T": (-5.6,-17.2,-23),
    "R": (-6.6,-17.4,-23),
    "E": (-7.6,-17.8,-22),
    "W": (-8.8,-18,-21.5), 
    "Q": (-9.6,-19,-21.5), 
    "C": (-7.7,-16.5,-24.8), 

}
global detectet_text
detectet_text = ""
Video_Recognition = "_Video Recognition_"
class Control(Frame):
    def __init__(self,master,video_source=0):
        super().__init__(master)
        print("========Init MAIN GUI CLASS======")
        self.grid()
        self.create_widgets()
        self.function = Function_Treeview()
        self.cognitive_service = Cognitive_Service()
        self.window_config()
        self.initMainMenu()
        self.vid = MyVideoCapture(video_source)
        self.video_frame()

        
    
    def window_config(self):
        self.master.title("Test Gcode Sender by John_Lex v1.0")
        self.master.geometry("1100x1300+400+1")
    
    def initMainMenu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="No exit")
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        menubar.add_cascade(label="Edit")

    def onExit(self):

        self.quit()

    def create_widgets(self):
        global get_home      
        self.menubar = Menu(self)                                                                  
        filemenu = Menu(self.menubar,tearoff=0)
        filemenu.add_command(label="New")

        #---------------TAB CONTROL BLOCK------------------------
        tab_control = ttk.Notebook(root)
        tab_control.grid(row=0,column=0)
        self.Manual_Control_Tab = ttk.Frame(tab_control,borderwidth=0)
        self.Text_Recognition_Block= ttk.Frame(tab_control)
        tab_control.add(self.Manual_Control_Tab, image=manual_control_gif)
        tab_control.add(self.Text_Recognition_Block,image=text_recognition_gif)
        #---------------END BLOCK------------------------

         #-----------------------------------------START DEFINE LABEL FRAME BLOCK--------------------------------------------------
        self.stepOne =LabelFrame(self.Manual_Control_Tab, text="Common Actions ")
        self.stepOne.grid(row=1, columnspan=10, sticky='W',padx=7, pady=5, ipadx=5, ipady=5)

        self.monitoring =LabelFrame(self.Manual_Control_Tab, text=" Status Real Time Block  ")
        self.monitoring.grid(row=2, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

        self.buzzer_control = LabelFrame(self.Manual_Control_Tab,text="Conection Control")
        self.buzzer_control.grid(row=0,column=0,columnspan=10,sticky='W',padx=7,pady=5,ipadx=5,ipady=5)

        self.terminal_frame = LabelFrame(self.Manual_Control_Tab,text="Real Time Terminal")
        self.terminal_frame.grid(row=0, column=9, columnspan=2, rowspan=30,sticky='NS', padx=5, pady=5)
        self.send_comand_frame = LabelFrame(self.Manual_Control_Tab,text="Send Comand")
        self.send_comand_frame.grid(row=30, column=8, columnspan=2, rowspan=20,sticky='NS', padx=5, pady=5)

        self.robotic_frame =LabelFrame(self.Manual_Control_Tab, text=" Robotic Arm Control Block  ")
        self.robotic_frame.grid(row=3, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        self.entry_gcode_comands=Entry(self.send_comand_frame,width=62)
        self.entry_gcode_comands.grid(row=0,column =0)

        self.set_position_label =LabelFrame(self.Manual_Control_Tab,text="Work Set Position")
        self.set_position_label.grid(row=5, columnspan=8, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        self.actual_position =LabelFrame(self.Manual_Control_Tab,text="Actual  Position")
        self.actual_position.grid(row=5, column=3, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        #-----------------------------------------END DEFINE LABEL FRAME BLOCK--------------------------------------------------

        #--------------------------------START CREATE ALL VIDGETS FROM MANUAL CONTROL TAB--------------------------------------

        Label(self.set_position_label,text='X').grid(row = 4 ,column=0)
        Label(self.set_position_label,text='mm').grid(row = 4 ,column=2)
        self.work_position_x = Entry(self.set_position_label,width=8)
        self.work_position_x.grid(row=4,column =1)

        Label(self.set_position_label,text='Y').grid(row =5 ,column=0)
        Label(self.set_position_label,text='mm').grid(row =5 ,column=2)
        self.work_position_y = Entry(self.set_position_label,width=8)
        self.work_position_y.grid(row=5,column =1)

        Label(self.set_position_label,text='Z').grid(row =6 ,column=0)
        Label(self.set_position_label,text='mm').grid(row =6 ,column=2)
        self.work_position_z = Entry(self.set_position_label,width=8)
        self.work_position_z.grid(row=6,column =1)
        #-----------------------------------------------------------------
        #actual feedback position 
        #work position block
        Label(self.actual_position,text='X').grid(row = 4 ,column=0)
        Label(self.actual_position,text='mm').grid(row = 4 ,column=2)
        self.actual_position_x = Entry(self.actual_position,width=8)
        self.actual_position_x.grid(row=4,column =1)

        Label(self.actual_position,text='Y').grid(row =5 ,column=0)
        Label(self.actual_position,text='mm').grid(row =5 ,column=2)
        self.actual_position_y = Entry(self.actual_position,width=8)
        self.actual_position_y.grid(row=5,column =1)

        Label(self.actual_position,text='Z').grid(row =6 ,column=0)
        Label(self.actual_position,text='mm').grid(row =6 ,column=2)
        self.actual_position_z = Entry(self.actual_position,width=8)
        self.actual_position_z.grid(row=6,column =1)

        #-----------------------------------------------------------------

        Label(self.set_position_label,text='X').grid(row = 4 ,column=0)
        Label(self.set_position_label,text='mm').grid(row = 4 ,column=2)
        self.work_position_x = Entry(self.set_position_label,width=8)
        self.work_position_x.grid(row=4,column =1)

        Label(self.monitoring,text="Connect Status Check").grid(row=3,column=0,sticky=W)
        self.state_label_1=Label(self.monitoring,text="Last Command").grid(row=4,column=0,sticky=W)
        
        #//////////////////////////////////////START DEFINE STATE BUTTONS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.get_state_button  = Button(self.stepOne,text="Get State",command=self.set_on_led,image=state,borderwidth=0).grid(row=0, columnspan=2,sticky=W,padx=5,pady=5,)
        self.rt_zero_button = Button(self.stepOne,text="Return to Zero",command=self.set_off_led,image=return1,borderwidth=0 ).grid(row=0,column=2,sticky=W,padx=5,pady=5,)
        self.reset_zero_button= Button(self.stepOne,text="Reset to Zero",command=self.set_on_led,image=zero,borderwidth=0 ).grid(row=1, columnspan=2,sticky=W,padx=5,pady=5,)
        self.home_machine_button = Button(self.stepOne,text="Home Machine",command=self.set_off_led,image=home,borderwidth=0 ).grid(row=1,column=2,sticky=W,padx=5,pady=5,)
        self.buz_on_button  = Button(self.buzzer_control,text="Connectfg",command=self.connect,image=connect,borderwidth=0).grid(row=0, columnspan=2,sticky=W,padx=5,pady=5,)
        self.buz_off_button = Button(self.buzzer_control,text="Disconnect",command=self.disconect,image=disconnect,borderwidth=0).grid(row=0,column=2,sticky=W,padx=5,pady=5,)
        self.home_machine_button = Button(self.stepOne,text="Help",command=self.set_off_led,image=help1, borderwidth=0 ).grid(row=3,column=0,sticky=W,padx=5,pady=5,)
        #-----------------------------------------------------------------------------------------------------------------------------
        self.answer=Text(self.monitoring, width=15, height=1, wrap=WORD)
        self.answer.grid(row=4, column=1, sticky=W)
        self.textBox7 = Text(self.monitoring,height=1,width=17)
        self.textBox7.grid(row=3,column=1)


        self.arm_left =Button(self.robotic_frame,image=x_down,borderwidth=0,command=partial(self.callback,3)).grid(row=2,column=0, sticky=W)
        self.arm_up =Button(self.robotic_frame,image =y_up ,borderwidth=0,command=partial(self.callback,1))
        self.arm_up.grid(row=1,column=1, sticky=W)
        self.arm_left =Button(self.robotic_frame,image =x_up ,borderwidth=0,command=partial(self.callback,4)).grid(row=2,column=2, sticky=W)
        self.arm_up =Button(self.robotic_frame,image=y_down,borderwidth=0,command=partial(self.callback,2)).grid(row=3,column=1, sticky=W)

        self.arm_left =Button(self.robotic_frame,image=z_down,borderwidth=0,command=partial(self.callback,6)).grid(row=1,column=5, sticky=W)
        self.arm_up =Button(self.robotic_frame,image =z_up ,borderwidth=0,command=partial(self.callback,5)).grid(row=3,column=5, sticky=W)
        
        Label(self.robotic_frame,text='Step Size XY').grid(row = 4 ,column=1)
        Label(self.robotic_frame,text='Step Size Z').grid(row = 5 ,column=1)
        Label(self.robotic_frame,text='Feed rate').grid(row = 6 ,column=1)

        self.size_xy=Entry(self.robotic_frame,width=8)
        self.size_xy.grid(row=4,column =2)
        self.size_z=Entry(self.robotic_frame,width=8)
        self.size_z.grid(row=5,column =2)
        self.feed_rate=Entry(self.robotic_frame,width=8)
        self.feed_rate.grid(row=6,column =2)
        Button(self.robotic_frame,text="Set Up").grid(row=6,column=3)

        #START of TEXT SCROLL Block--------------------------------
        self.text1 = Text(self.terminal_frame, height=40, width=48)
        self.scroll = Scrollbar(self.terminal_frame, command=self.text1.yview, orient=VERTICAL, width=30 )
        self.scroll.config(command=self.text1.yview)
        

        self.text1.configure(yscrollcommand=self.scroll.set)
        self.entry = Entry(self.terminal_frame, width = 40)
        self.entry.grid(row=0,column=0,sticky=W)
        self.text1.grid(row=0,column=0,sticky=W)
        self.scroll.grid(row=0,column=1,sticky=E)
        #STOP----------------------------------------------------------
        #command=self.send_command(self.entry_gcode_comands.get())
        
        
        self.send_button = Button(self.send_comand_frame,image=send,command=self.send_command,borderwidth=0).grid(row=0,column=1,sticky=W,padx=5,pady=5)
        #--------------------------------END CREATE ALL VIDGETS FROM MANUAL CONTROL TAB--------------------------------------
        #######################################################################################################################
        #---------------------------------START CREATE WIDGET FROM VIDEOCAPTURE TAB-------------------------------------------

       #---------//////////////////START CREATE LABEL FRAME FOR VIDEORECOGNITION TAB\\\\\\\\\\\\\\\\\\\\\\\\\-------------
        global Video_Recognition
        self.video_recognition_main_label=LabelFrame(self.Text_Recognition_Block, text=Video_Recognition) #done
        self.video_recognition_main_label.grid(row=0,column=0,sticky=W,padx=5,pady=5,rowspan=1)

        self.control_panel=LabelFrame(self.video_recognition_main_label, text="Control Panel") #done
        self.control_panel.grid(row=0,column=0,sticky=W,rowspan=1)
        
        self.connection_control_video_label=LabelFrame(self.control_panel, text="Video Connection Control") #done
        self.connection_control_video_label.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.Detect_Mode_label=LabelFrame(self.control_panel, text="Detect Mode")
        self.Detect_Mode_label.grid(row=1,column=0, sticky='W',padx=7, pady=5, ipadx=5, ipady=5)

        self.Text_recognition_Metod_label=LabelFrame(self.control_panel, text="Detect Text from URL Photo")
        self.Text_recognition_Metod_label.grid(row=2,column=0, sticky='W',padx=7, pady=5, ipadx=5, ipady=5)

        self.detect_text_from_camera=LabelFrame(self.control_panel, text="Detect Text from Camera")
        self.detect_text_from_camera.grid(row=3,column=0, sticky='W',padx=7, pady=5, ipadx=5, ipady=5)


        self.Video_Detection_Label=LabelFrame(self.video_recognition_main_label, text="Video Detection Block")#done
        self.Video_Detection_Label.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        self.Video_Frame_Label=LabelFrame(self, text="Video Frame")
        self.Video_Frame_Label.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        #-----------------START Create History treeview start--------------------
        self.treeview_frame = LabelFrame(self.video_recognition_main_label, text="Recognized Text List")
        self.treeview_frame.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        self.execute_buttons_frame = LabelFrame(self, text="Execute Buttons")
        self.execute_buttons_frame.grid(row=14,column=0,sticky=W,padx=5,pady=5)

        self.video_regonition_connect_block = LabelFrame(self, text="Camera Connection Control")
        self.video_regonition_connect_block .grid(row=4,column=1,sticky=W,padx=5,pady=5)

        self.Main_Detection_Label=LabelFrame(self.treeview_frame, text="Main Execution Panel")
        self.Main_Detection_Label.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        

        self.video_recognition_terminal=LabelFrame(self.video_recognition_main_label, text="Real time Execution Terminal")
        self.video_recognition_terminal.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.actual_text_to_print=LabelFrame(self.video_recognition_terminal, text="Actual Text to Print ")
        self.actual_text_to_print.grid(row=0,column=0,sticky=W,padx=5,pady=5)


        #-----------------END History treeview start--------------------
        #---------//////////////////END CREATE LABEL FRAME FOR VIDEORECOGNITION TAB\\\\\\\\\\\\\\\\\\\\\\\\\-------------
        
        #---------------------START CREATE LABEL WITH ACUTAL TEXT TO PRINT--------------------------------
        Label(self.actual_text_to_print,text='Actual Text->').grid(row =1 ,column=0)
        self.actual_text_to_print=Entry(self.actual_text_to_print,width=35)
        self.actual_text_to_print.grid(row=1,column =1,sticky=W,padx=5,pady=5)
        

        #---------------------START CREATE treeview FOR VIDEORECOGNITION TAB---------------------------------------------
        global treeview_list
        treeview_list =ttk.Treeview(self.treeview_frame,columns=("Type of Detection",'Name of Photo','Detected Text','Execution Status'),height=10)
        treeview_list.column('#0',anchor=CENTER,width=40)
        treeview_list.column('Type of Detection',anchor=CENTER,width=170)
        treeview_list.column('Name of Photo',anchor=CENTER,width=130)
        treeview_list.column('Detected Text',anchor=CENTER,width=200)
        treeview_list.column('Execution Status',anchor=CENTER,width=100)

        treeview_list.heading('#0',text='ID')
        treeview_list.heading('Type of Detection',text='Type of Detection')
        treeview_list.heading('Name of Photo',text='Name of Photo')
        treeview_list.heading('Detected Text',text='Detected Text')
        treeview_list.heading('Execution Status',text='Execution Status')

        

        treeview_list.grid(row=0,column=0,padx=10,pady=7,rowspan=2)
        #-------------------------define level and sublevel-----------------------
        self.handwritten_text_detected_list=treeview_list.insert("",1,text="",values=("HANDWRITTEN_TEXT"," ","",""))
        self.url_text_detected_list=treeview_list.insert("",2,text="",values=("URL_TEXT"," ","",""))
        self.object_text_detected_list=treeview_list.insert("",3,text="",values=("OBJECT_TEXT"," ","",""))
        #----------------------------START processing TOUCH EVENT FROM TREEVIEW--------------------------------------

        treeview_list.bind("<Double-1>",self.double_click_view_information)
        treeview_list.bind("<<TreeviewSelect>>",self.intermediate_one_click_treeview)


        #-------------------------Define level 2---------------------------------
        self.hnd_txt_test = treeview_list.insert(self.handwritten_text_detected_list,"end",text="hnd_txt_1",values=("","Test Photo Name","","Done"))
        self.hnd_txt_test_leve2 = treeview_list.insert(self.hnd_txt_test,"end",text="hnd_txt_1",values=("","","Victor a venit","Done"))
        self.hnd_txt_test_leve2 = treeview_list.insert(self.hnd_txt_test,"end",text="hnd_txt_1",values=("","","La universitate","Done"))
        #-------------------------------------------------------------------------
        # self.treeview_list.insert(self.lista,"end",values=("","Primul rind detectat din fotografie","Done","Recognised by Server"))
        # self.treeview_list.insert(self.lista,"end",values=("","Al doilea rind detectat din fotografie","Done","Recognised by Server"))

        #------------------------------------------------------------------------

        #-------------------------------------------------------------------------
  
        self.delete=Button(self.Main_Detection_Label,text="Delete row",borderwidth=1,command=self.intermediate_delete_selectet_treeview).grid(row=1,column=0, sticky=W,padx=5,pady=5)
        self.print_text=Button(self.Main_Detection_Label,text="Type on keyboard",borderwidth=1,command = self.intermediate_detect_type_on_keyboard).grid(row=1,column=1, sticky=W,padx=5,pady=5)

        #---------------------START CREATE CONNECT BUTTONS FOR VIDEORECOGNITION TAB---------------------------------------------
        self.connect_camemera_button=Button(self.connection_control_video_label,text="Connect Camera",borderwidth=1)
        self.connect_camemera_button.grid(row=0,column=0, sticky=W,padx=5,pady=5)
        self.disconnect_camemera_button=Button(self.connection_control_video_label,text="Disconnect Camera",borderwidth=1)
        self.disconnect_camemera_button.grid(row=0,column=1, sticky=W,padx=5,pady=5)
        #---------------------START CREATE RADIOBUTTONS FOR VIDEORECOGNITION TAB------------------------------------------------
        global detection_mode
        self.Object_Metod_recognition= Radiobutton(self.Detect_Mode_label,text="Object Recognition", variable=detection_mode, value=2)
        self.Object_Metod_recognition.grid(row=1,column=0,sticky=W)
        self.Handwritten_Metod_recognition= Radiobutton(self.Detect_Mode_label,text="Text    Detection", variable=detection_mode, value=1)
        self.Handwritten_Metod_recognition.grid(row=0,column=0,sticky=W)

        #---------------------START CREATE URL TEXT DETECTION--------------------------------------
        Label(self.Text_recognition_Metod_label,text='Photo URL->').grid(row =0 ,column=0)
        self.url_to_detection=Entry(self.Text_recognition_Metod_label,width=25)
        self.url_to_detection.grid(row=0,column =1,sticky=W)

        Label(self.Text_recognition_Metod_label,text='Name of Photo->').grid(row =1 ,column=0)
        self.name_url_to_detection=Entry(self.Text_recognition_Metod_label,width=25)
        self.name_url_to_detection.grid(row=1,column =1,sticky=W)

        self.detect_url_text=Button(self.Text_recognition_Metod_label,text="Detect Text from URL",borderwidth=1,command = self.intermediate_detect_from_URL)
        self.detect_url_text.grid(row=2,column=0, sticky=W,padx=5,pady=5)
        self.detect_url_text=Button(self.Text_recognition_Metod_label,text="Type on Keyboard",borderwidth=1,command = self.intermediate_detect_type_on_keyboard)
        self.detect_url_text.grid(row=2,column=1, sticky=W,padx=5,pady=5)
        #-----------------------START CREATE DETECT TEXT FROM CAMERA---------------------------------------------
        global name_text_CAMERA_to_detection
        Label(self.detect_text_from_camera,text='Name of Photo->').grid(row =1 ,column=0)
        name_text_CAMERA_to_detection=Entry(self.detect_text_from_camera,width=25)
        name_text_CAMERA_to_detection.grid(row=1,column =1,sticky=W)
        self.detect_camera_text=Button(self.detect_text_from_camera,text="Detect Text",borderwidth=1)
        self.detect_camera_text.grid(row=2,column=0, sticky=W,padx=5,pady=5)
        #-----------------------START CREATE TERMINAL FOR VIDEO DETECTION BLOCK------------------------------------
        #START of TEXT SCROLL Block--------------------------------
        global video_terminal
        video_terminal= Text(self.video_recognition_terminal, height=15, width=40)
        self.scroll_1 = Scrollbar(self.video_recognition_terminal, command=video_terminal.yview, orient=VERTICAL, width=30 )
        self.scroll_1.config(command=video_terminal.yview)
        
        video_terminal.insert(0.0,"wdadaw")
        video_terminal.configure(yscrollcommand=self.scroll_1.set)
        video_terminal.grid(row=1,column=0,sticky=W)
        self.scroll_1.grid(row=1,column=1,sticky=E)
        #STOP----------------------------------------------------------
        global detectet_text

        #---------------------------------END CREATE WIDGET FROM VIDEOCAPTURE TAB-------------------------------------------  
        #---------------------------------END CREATE WIDGET FROM VIDEOCAPTURE TAB-------------------------------------------
    def intermediate_get_id(self,*args):
        self.function.id_get_from_treeview()
    def intermediate_one_click_treeview(self,*args):
        self.function.id_get_from_treeview()
    def intermediate_delete_selectet_treeview(self,*args):
        self.function.delete_selected()
    def double_click_view_information(self,*args):
        #self.function.print_information_treeview(text_input=self.function.form_text_val(id_1=self.function.id_get_from_treeview()))
        self.function.get_item_text(id_1=id_1)
    def intermediate_detect_from_URL(self,*args):
        self.cognitive_service.recognize_input_text(mode_detection=2,name_photo=self.name_url_to_detection.get(),photo_url=self.url_to_detection.get())
    def intermediate_detect_from_locale_photo(self,*args):
        global name_text_CAMERA_to_detection
        self.cognitive_service.recognize_input_text(mode_detection=1,name_photo=name_text_CAMERA_to_detection,photo_url="NONE")
    def intermediate_detect_type_on_keyboard(self,*args):
        print("0404040404404004-{}".format(detectet_text))
        self.function.type_on_keyboard(word=detectet_text)
    def change_to_rus(self):
        self.btn_snapshot=Button(self.Main_Detection_Label, text="Сделать снимок", width=14, command=self.snapshot)
        self.btn_snapshot.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        self.print_text=Button(self.Main_Detection_Label,text="Напечатать текст",borderwidth=1,command = self.intermediate_detect_type_on_keyboard,width=14).grid(row=1,column=1, sticky=W,padx=5,pady=5)
        self.delete=Button(self.Main_Detection_Label,text="Удалить строку ",borderwidth=1,command=self.intermediate_delete_selectet_treeview,width=14).grid(row=1,column=0, sticky=W,padx=5,pady=5)
        self.Main_Detection_Label=LabelFrame(self.treeview_frame, text="Панель основного исполнения")
        self.Main_Detection_Label.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        self.video_recognition_main_label=LabelFrame(self.Text_Recognition_Block, text="Видео Распознавание") #done
        self.video_recognition_main_label.grid(row=0,column=0,sticky=W,padx=5,pady=5,rowspan=1)
    def change_to_ro(self):
        self.btn_snapshot=Button(self.Main_Detection_Label, text="Captureaza Imaginea", width=14, command=self.snapshot)
        self.btn_snapshot.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        self.print_text=Button(self.Main_Detection_Label,text="Tapează textul",borderwidth=1,command = self.intermediate_detect_type_on_keyboard,width=14).grid(row=1,column=1, sticky=W,padx=5,pady=5)
        self.delete=Button(self.Main_Detection_Label,text="Șterge",borderwidth=1,command=self.intermediate_delete_selectet_treeview,width=14).grid(row=1,column=0, sticky=W,padx=5,pady=5)
        self.Main_Detection_Label=LabelFrame(self.treeview_frame, text="Panelul Principal")
        self.Main_Detection_Label.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        self.video_recognition_main_label=LabelFrame(self.Text_Recognition_Block, text="Video Recunoaștere") #done
        self.video_recognition_main_label.grid(row=0,column=0,sticky=W,padx=5,pady=5,rowspan=1)
    def change_to_eng(self):
        self.btn_snapshot=Button(self.Main_Detection_Label, text="Snapshot", width=14, command=self.snapshot)
        self.btn_snapshot.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        self.print_text=Button(self.Main_Detection_Label,text="Type on keyboard",borderwidth=1,command = self.intermediate_detect_type_on_keyboard,width=14).grid(row=1,column=1, sticky=W,padx=5,pady=5)
        self.delete=Button(self.Main_Detection_Label,text="Delete",borderwidth=1,command=self.intermediate_delete_selectet_treeview,width=14).grid(row=1,column=0, sticky=W,padx=5,pady=5)
        self.Main_Detection_Label=LabelFrame(self.treeview_frame, text="Main Panel")
        self.Main_Detection_Label.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        self.video_recognition_main_label=LabelFrame(self.Text_Recognition_Block, text="Video Detection") #done
        self.video_recognition_main_label.grid(row=0,column=0,sticky=W,padx=5,pady=5,rowspan=1)
    def video_frame(self):
        # Create a canvas that can fit the above video source size
        global Video_Frame_Label
        
        self.canvas = Canvas(self.Video_Detection_Label, width = self.vid.width, height = 350)
        print(self.vid.width) 
        self.canvas.grid(row=0,column=0)
        # Button that lets the user take a snapshot
        self.buz_off_button = Button(self.buzzer_control,text="Disconnect",command=self.disconect,image=disconnect,borderwidth=0).grid(row=0,column=2,sticky=W,padx=5,pady=5,)
        self.btn_snapshot=Button(self.Main_Detection_Label, text="Snapshot", width=10, command=self.snapshot)
        self.btn_snapshot.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        self.btn_english=Button(self.Main_Detection_Label, text="English", image = en_flag, command=self.change_to_eng,borderwidth=0)
        self.btn_english.grid(row=1,column=3)
        self.btn_rom=Button(self.Main_Detection_Label, text="Româna", image = rom_flag, command=self.change_to_ro,borderwidth=0)
        self.btn_rom.grid(row=1,column=4)
        self.btn_rus=Button(self.Main_Detection_Label, text="Русский",image = rus_flag,command=self.change_to_rus,borderwidth=0)
        self.btn_rus.grid(row=1,column=5)
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
    def onreturn(self):
        print("b")
        
    
    def connect(self):
        print("connect")
        print("connect")
        self.textBox7.delete(0.0,END)
        self.text1.insert(0.0,">>>"+"Connect to GRBL"+"\n")
        self.textBox7.insert(0.0,'Connect to GRBL')
        start_grbl="\r\n\r\n"
        ser.write(start_grbl.encode())
        time.sleep(2)   # Wait for grbl to initialize 
#         ser.flushInput()  # Flush startup text in serial input
        chechk_status ="$$"
        ser.write(chechk_status.encode())
        grbl_connect_out =ser.readlines() # Wait for grbl response with carriage return
#         grbl_connect_out =grbl_connect_out.decode()
        grbl_connect_out = [el.decode() for el in grbl_connect_out]
        grbl_connect_out =' '.join(grbl_connect_out)
        self.text1.insert(0.0,">>>"+grbl_connect_out+"\n")
    def disconect(self):
        print("disconnect")
        self.textBox7.delete(0.0,END)
        self.textBox7.insert(0.0,'Disconnect GRBL')
    def set_on_led(self):
        i=0
        i=str(i)
        self.function.printw()
        self.answer.delete(0.0,END)
        self.text1.insert(0.0,">>>"+"LED is ON"+"\n")
        print("LED is ON")
        self.answer.insert(0.0,'LED')
        i=int(i)
        i=i+1
    def set_off_led(self):
        print("LED is OFF")
        self.answer.delete(0.0,END)
        self.answer.delete(0.0)
        self.text1.insert(0.0,">>>"+"LED is OFF"+"\n")
        self.answer.insert(0.0,'LED is OFF')
    def send_command(self,*args):
        print("send command")
        sa = self.entry_gcode_comands.get()
        self.text1.insert(0.0,">>>"+sa+"\n")
        sa=sa+"\n"
        ser.write(sa.encode())
        grbl_out=ser.readlines()
        grbl_out = [el.decode() for el in grbl_out]
        grbl_out =' '.join(grbl_out)
        print(":"+grbl_out)
        self.text1.insert(0.0,">>>"+grbl_out+"\n")
    def sas(self):
        self.text1.insert(0.0,"dwadawd")
    def get_xy(self):
        return self.size_xy
    def get_xy(self):
        return self.feed_rate
    def callback(self,value,*args):
        global send_1
        xy=self.size_xy.get()
        feed=self.feed_rate.get()
        z =self.size_z.get()
        if value == 1:#UP Y
            self.answer.insert(0.0,"G21G91Y"+xy+"F"+feed+"\n")
            send="G21G91Y"+xy+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
            self.text1.insert(0.0,">>>"+send_1+"\n")
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")
            
        if value == 2:#down Y-
            fr =-int(xy)
            self.answer.insert(0.0,"G21G91Y"+str(fr)+"F"+feed+"\n")
            send="G21G91Y-"+xy+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
            self.text1.insert(0.0,">>>"+send_1+"\n")
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")
            
        if value == 3:#Left -X
            xyy = -int(xy)
            self.answer.insert(0.0,"G21G91X"+str(xyy)+"F"+feed+"\n")
            send="G21G91X-"+xy+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
            self.text1.insert(0.0,">>>"+send_1+"\n")
            
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")
        if value == 4:#Right +X
            self.answer.insert(0.0,"G21G91X"+xy+"F"+feed+"\n")
            send="G21G91X"+xy+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
            self.text1.insert(0.0,">>>"+send_1+"\n")
            
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")

        if value == 5:#Z+
            self.answer.insert(0.0,"G21G91Z"+z+"F"+feed+"\n")
            send="G21G91Z"+z+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
            
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")
        if value == 6:#z-
            z1 = -int(z)
            self.answer.insert(0.0,"G21G91Z"+str(z1)+"F"+feed+"\n")
            send="G21G91Z-"+z+"F"+feed
            self.text1.insert(0.0,">>>"+send+"\n")
                
            print(send)
            print(send_1)
            send =send+"\n"
            send_1=send_1+"\n"
            ser.write(send.encode())
            grbl_out = ser.readlines()
            ser.write(send_1.encode())
            grbl_out_1 = ser.readlines()
            grbl_out_1 = [el.decode() for el in grbl_out_1]
            grbl_out_1 =' '.join(grbl_out_1)

            grbl_out = [el.decode() for el in grbl_out]
            grbl_out =' '.join(grbl_out)
      
            print(":"+grbl_out)
            print(":"+grbl_out_1)
            self.text1.insert(0.0,">>>"+grbl_out+"\n")
            self.text1.insert(0.0,">>>"+grbl_out_1+"\n")
    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        global name_text_CAMERA_to_detection
        if ret:
              cv2.imwrite("frame-" + name_text_CAMERA_to_detection.get()+ ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        self.intermediate_detect_from_locale_photo()
        #self.function.typing_word(string=text_rec)
        print("[INFO] Text to tipyng ->{}".format(name_text_CAMERA_to_detection))
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.master.after(self.delay, self.update)
        
class Function_Treeview:
    def __init__(self):
        print("========Init Treeview Function Class=======")
        self.main_window =Arduino_Control

    def let(self,letter): #find position of letter from letter_Pos_dictionary
        X = pos_leter[letter][0]
        Y = pos_leter[letter][1]
        Z =pos_leter[letter][2]
        return X,Y,Z
    def send_to_type(self,letter,pos_x_letter , pos_y_letter, pos_z_letter):#send to robotic arm via usb interface pos x,y,z to type
        comand_to_roboto = "G21G91G1X"+str(pos_x_letter)+"Y"+str(pos_y_letter)+"Z"+str(pos_z_letter)+"F5000"+"\n"
        comand_to_roboto_back = "G21G91G1X"+str(-pos_x_letter)+"Y"+str(-pos_y_letter)+"Z"+str(-pos_z_letter)+"F5000"+"\n"
        ser.write(comand_to_roboto.encode())
        grbl_out = ser.readlines()
        ser.write(comand_to_roboto_back.encode())
        grbl_out_1 =ser.readlines()
        grbl_out_1 = [el.decode() for el in grbl_out_1]
        grbl_out_1 =' '.join(grbl_out_1)

        grbl_out = [el.decode() for el in grbl_out]
        grbl_out =' '.join(grbl_out)
        
        print("{}:{}".format(letter,grbl_out))
        print("{} Back_>:{}".format(letter,grbl_out_1))
    def type_on_keyboard(self,word):
        for i in word:
            pos_x_letter , pos_y_letter, pos_z_letter = self.let(i)
            self.send_to_type(letter = i,pos_x_letter= pos_x_letter, pos_y_letter=pos_y_letter, pos_z_letter=pos_z_letter)
    def print_function_name(self,*atgs): 
        print(inspect.stack()[1][3])
    #divide text_val in two groups: field text and field values
    def split_textval(self,*args,text_val):
        self.print_function_name()
        field_lst = text_val.split(';')
        field_text =field_lst[0]
        field_value =field_lst[1:]
        return field_text, field_text  

    def add_element(self,*args,id_1,element):
        self.print_function_name()
        global treeview_list
        if type(element) ==str:
            field_text, field_vals =self.split_textval(element)
            treeview_list.insert(id_1,'end',text = field_text,values = field_vals)
        elif type(element) == list:
            field_text, field_vals =self.split_textval(element[0])
            sub_id = treeview_list.insert(id_1,'end',text=field_text, values=field_vals)
            for sub_element in element[1:]:
                add-element(sub_id,sub_element)
    
    #create list from treeview children
    def get_item_text(self,*args,id_1):
        self.print_function_name
        global treeview_list
        st_loc = self.form_text_val(id_1=id_1)
        children  =treeview_list.get_children(id_1)
        if len(children)>0:
            st_loc = "[|"+st_loc
            for child in children:
                st_loc +="|"+self.get_item_text(id_1=child)
            st_loc +="|]"
            print(st_loc)
            return st_loc
        else:
            print(st_loc)
            return st_loc
    def print_information_treeview(self,*arg,text_input):
        self.print_function_name()
        print (text_input)

    def delete_selected(self):
        self.print_function_name()
        global treeview_list
        global id_1
        id_1 =self.id_get_from_treeview()
        treeview_list.delete(id_1)

    def id_get_from_treeview(self,*args):
        self.print_function_name()
        global treeview_list
        global id_1
        id_1 = treeview_list.selection()
        text_val =self.form_text_val(id_1=id_1) #optional just for test 
        print(id_1)
        return id_1

    def form_text_val(self,*args,id_1):
        self.print_function_name()
        global treeview_list
        field_text = treeview_list.item(id_1)['text']
        field_vals = treeview_list.item(id_1)['values']
        text_val =field_text
        if len(field_vals)>0:
            for num in range(len(field_vals)):
                field_vals[num] = str(field_vals[num])
            text_val +=";"+";".join(field_vals)
        print("Text value =",text_val)
        return text_val
    def typing_word(self,string):
        """--------------------------------------START AUTOMATE DETECTION OF LETTER FROM KEYBOARD AND SEND IT TO CNN----------------------------------------- """
        cap = cv2.VideoCapture(vide_source)
        print("1===========================================")
        global image_good
        global ii,y_diff,x_diff,not_detected_letter,not_detected_letter_pos_dictionary,orderet_lt_dict,detectet_letter,pos_letter_list,pos_dict,centroid_dict,x,y,w,h,cx,cy
        printed_text=" "
        global inRange_count
        global distance
        while not image_good:
            while True:
                ret, frame = cap.read()
                contourIM = frame.copy()
                gray = cv2.cvtColor(contourIM, cv2.COLOR_BGR2GRAY)
                ret, threshold = cv2.threshold(gray,165,255,cv2.THRESH_BINARY)
                kernel33 = np.ones((3,3),np.uint8)
                kernel22 = np.ones((2,2),np.uint8)
                mask = cv2.dilate(threshold,kernel33,iterations = 4)
                contours,_ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                contours_area = pd.Series([cv2.contourArea(contour) for contour in contours])
                contours_area = contours_area[contours_area > 120]
                contours_area = contours_area[contours_area < 390]
                contours = [contours[i] for i in contours_area.index]
                contours_bb = [cv2.boundingRect(cnt) for cnt in contours]
                max_score = {}
                loc = {}
                for i,(x,y,w,h) in enumerate(contours_bb):  # (x,y) is the top left corner of the box
                    # make the bounding box a square
                    if h > w:
                        diff = h-w
                        w = h
                        x -= (diff/2 + 1)
                    if w > h:
                        diff = w-h
                        h = w
                        y -= diff/2
                    char_img = gray[int(y):int(y)+int(h),int(x):int(x)+int(w)].copy()
                    if char_img.shape[0] == 0 or char_img.shape[1] == 0:
                        continue
                    char_img = cv2.resize(char_img, (30,30), interpolation=cv2.INTER_CUBIC)
                    char_img = char_img.astype(np.float32)
                    char_img = char_img/255*2 -1 #shape is now (30,30)
                    char_img = np.expand_dims(char_img, axis=0) #shape is now (1,30,30)
                    char_img = char_img[..., np.newaxis] #shape is now (1,30,30,1)
                    predicted_vec = model.predict(char_img)
                    score = np.amax(predicted_vec, axis=1)[0]
                    prediction = char_names[np.argmax(predicted_vec)]
                    if score > max_score.get(prediction, 0) and prediction in capital_letters:
                        max_score[prediction] = score
                        loc[prediction] = (x,y,w,h)    
                for i,c in enumerate(loc):
                        x,y,w,h = loc[c]
                        d=loc[c]
                        contourIM = cv2.rectangle(contourIM,(int(x),int(y)),(int(x)+int(w),int(y)+int(h)),(0,255,0),1)
                        contourIM = cv2.putText(contourIM, '{}'.format(c), (int(x),int(y)-2), \
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255))
                        ii = i
                if ii>=15:
                    print("----Find {} letters.-----".format(ii))
                    break
                cv2.imshow('contourIM',contourIM)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.imshow('contourIM',contourIM)
            
            while True:
                input1 = input("Does this image capture all the letters correctly?  y or n \n").lower()
                if input1 == 'yes' or input1 == 'y':
                    image_good = True
                    break
                elif input1 == 'no' or input1 == 'n':
                    image_good = False
                    print("\nWhen the video captures all the letters correctly, select the video window and press 'q'")
                    break
                else:
                    print('input not recognized')
        """--------------------------------------STOP AUTOMATE DETECTION OF LETTER FROM KEYBOARD AND SEND IT TO CNN----------------------------------------- """
        """############################################################################################################################ """
        """--------------------------------------START TRANSFORM RECOGNIZET LETTER FROM 3D POSITION TO 2D POSITION -------------------------- """
        print(":->OK.")   
        cv2.destroyAllWindows()
        cap.release()
        print("2===========================================")
        cap_2 = cv2.VideoCapture(vide_source)
        print(":->Transform detected letter from 3D to 2D...")
        global se
        for c in loc:
            x,y,w,h = loc[c]
            pos_letter_list.append((c,x,y,w,h))
            detectet_letter.append(c)
            print("{}-{}".format(se,pos_letter_list[se]))
            se = se+1
            cx, cy = x+w/2, y+h/2
            cx =cx +7
            cy = cy +7
            imgPt_c = np.array([[cx],[cy],[1 ]])
            worldPt_c = k_inv.dot(depth_cam2key * imgPt_c)
            centroid_dict[c] = (worldPt_c[0,0], worldPt_c[1,0])
            pos_dict[c] =(x,y,x+w,y+h,cx,cy,w,h)
        detectet_letter.sort()
        detectet_letter.pop(0)
        print(":->OK.")
        lol = 0
        for s,r in enumerate(detectet_letter):
            orderet_lt_dict[r] = pos_dict[r]
        """--------------------------------------STOP TRANSFORM RECOGNIZET LETTER FROM 3D POSITION TO 2D POSITION -------------------------- """
        """############################################################################################################################ """
        """ --------------------------------------START ALGORITM TO FIND ALL NOT RECOGNIZED LETTER------------------------------------- """
        print(":->___INIT AUTOCOMPLETE KEYBOARD NOT DETECTED LETTER ALGORITM...")
        print(":->Maping all detected letter...")
        for i in detectet_letter:
            sosed_r = sosedi[i][1]
            sosde_l =sosedi[i][0]
            if sosde_l =="  ":
                ii = i in orderet_lt_dict
                if ii == False:
                    not_detected_letter.append(i)
                    drawing_letter_pos.append(drawing_letter(i,sosde_l,(0,0,0,0),sosed_r,"not_found"))
                else:
                    ss = sosed_r in orderet_lt_dict
                    if ss == False:
                        print("------{}".format(sosed_r in orderet_lt_dict))
                        not_detected_letter.append(sosed_r)
                        drawing_letter_pos.append(drawing_letter(i,sosde_l,(0,0,0,0),sosed_r,"not_found"))
                    else:
                        print("------{}".format(sosed_r in orderet_lt_dict))
                        drawing_letter_pos.append(drawing_letter(i,sosde_l,(0,0,0,0),sosed_r,orderet_lt_dict[sosed_r]))
            if sosed_r == "  ":
                ri = i in orderet_lt_dict
                if ri== False:
                    not_detected_letter.append(i)
                    drawing_letter_pos.append(drawing_letter(i,sosde_l,"not_found",sosed_r,(0,0,0,0)))
                else:
                    rr = sosde_l in orderet_lt_dict
                    if rr == False:
                        not_detected_letter.append(sosde_l)
                        drawing_letter_pos.append(drawing_letter(i,sosde_l,"not_found",sosed_r,(0,0,0,0)))
                    else:
                        drawing_letter_pos.append(drawing_letter(i,sosde_l,orderet_lt_dict[sosde_l],sosed_r,(0,0,0,0)))
            else:
                    ss = sosed_r in orderet_lt_dict
                    if ss == False:
                        not_detected_letter.append(sosed_r)
                        sss =sosde_l in orderet_lt_dict
                        if sss == False:
                            not_detected_letter.append(sosde_l)
                            drawing_letter_pos.append(drawing_letter(i,sosde_l,"not_found",sosed_r,"not_found"))
                        else:
                            drawing_letter_pos.append(drawing_letter(i,sosde_l,orderet_lt_dict[sosde_l],sosed_r,"not_found"))
                    else:
                        sr = sosde_l in orderet_lt_dict
                        if sr == False:
                            not_detected_letter.append(sosde_l)
                            drawing_letter_pos.append(drawing_letter(i,sosde_l,"not_found",sosed_r,orderet_lt_dict[sosed_r]))
                        else:
                            drawing_letter_pos.append(drawing_letter(i,sosde_l,orderet_lt_dict[sosde_l],sosed_r,orderet_lt_dict[sosed_r]))
            left_len = len(drawing_letter_pos[lol].Left_Letter)
            r_len = len(drawing_letter_pos[lol].Rght_letter)
            if lol>14:
                if left_len ==1 and r_len ==1:
                    left =drawing_letter_pos[lol].lt_lt_pos
                    right =drawing_letter_pos[lol].rt_lt_pos
                    if left !="not_found" and right !="not_found":
                        dist_x_sus =  float(right[0])-float(left[0])
                        distance = dist_x_sus
            lol = lol+1
        print(":->OK.")   
        print("3===========================================")    
        """ --------------------------------------STOP ALGORITM TO FIND ALL NOT RECOGNIZED LETTER------------------------------------- """
        """############################################################################################################################ """
        """----------------------------------------START AUTO FIND NOT RECOGNIZED LETTER POSITION---------------------------------------"""
        for k,i in enumerate(not_detected_letter):
            if not_detected_letter[k]=="  " or not_detected_letter[k]=="1":
                not_detected_letter.pop(k)
        print(":->Find all not dected letter and start automaping for this letter...")
        print("-----Not detectet letter->{}".format(not_detected_letter))
        print(not_detected_letter)
        left_sosed = False
        not_detected_letter = [el for el, _ in groupby(not_detected_letter)]
        not_detected_letter_pos =["1"]
        for k,g in enumerate(not_detected_letter):
            if not_detected_letter[k]== "  ":
                not_detected_letter.pop(k)
        for g,i in enumerate(not_detected_letter):
            left_sosed = False
            if sosedi[i] !="  ":
                des =sosedi[i]
                if len(des[0]) == 1:
                    near_bool = des[0] in orderet_lt_dict
                    if near_bool == True:
                        print("Litera->{} sosed->{}".format(i,des[0]))
                        left_sosed_pos = orderet_lt_dict[des[0]] #return tuple (x,y,x+w,y+h,cx,cy)
                        distance1 = distance /2
                        x_pos_recon_letter =(left_sosed_pos[0])+distance1
                        y_pos_recon_letter =left_sosed_pos[1]
                        w_pos_recon_letter =left_sosed_pos[6]
                        h_pos_recon_letter =left_sosed_pos[7]
                        x2 =(x_pos_recon_letter+w_pos_recon_letter)
                        y2 =y_pos_recon_letter+h_pos_recon_letter
                        not_detected_letter_pos.append((i,x_pos_recon_letter,y_pos_recon_letter,x2,y2))

                        cx, cy = x_pos_recon_letter+w_pos_recon_letter/2, y_pos_recon_letter+h_pos_recon_letter/2
                        cx =cx +7
                        cy = cy +7
                        orderet_lt_dict[i] = (x_pos_recon_letter,y_pos_recon_letter,x2,y2,cx,cy,w_pos_recon_letter,h_pos_recon_letter)
                        print("---Added element->{}".format(orderet_lt_dict[i]))
                        detectet_letter.append(i)
                        left_sosed = True
                        # not_detected_letter.pop(g)
                if len(des[1]) == 1:
                    if left_sosed == False:
                        if len(des[1])==1:
                            near_bool = des[1] in orderet_lt_dict
                            if near_bool ==True:
                                distance2 = distance /2
                                print("Litera->{} sosed->{}".format(i,des[1]))
                                right_sosed_pos =orderet_lt_dict[des[1]]
                                x_pos_recon_letter =right_sosed_pos[0]-distance2
                                y_pos_recon_letter =right_sosed_pos[1]
                                w_pos_recon_letter =right_sosed_pos[2]-right_sosed_pos[0]
                                h_pos_recon_letter =right_sosed_pos[3]-right_sosed_pos[1]
                                x2 =(x_pos_recon_letter+w_pos_recon_letter)
                                y2 =y_pos_recon_letter+h_pos_recon_letter
                                not_detected_letter_pos.append((i,x_pos_recon_letter, y_pos_recon_letter,x2,y2))
                                cx, cy = x_pos_recon_letter+w_pos_recon_letter/2, y_pos_recon_letter+h_pos_recon_letter/2
                                cx =cx +7
                                cy = cy +7
                                orderet_lt_dict[i] = (x_pos_recon_letter,y_pos_recon_letter,x2,y2,cx,cy,w_pos_recon_letter,h_pos_recon_letter)
                                print("---Added element->{}".format(orderet_lt_dict[i]))
                                # not_detected_letter.pop(g)
                                left_sosed = False
                                detectet_letter.append(i)
                if len(des[1]) != 1 and len(des[0]) != 1:
                    not_detected_letter.append(i)
        for i in string:
            resa = i in detectet_letter
            if resa == False:
                string = string.replace(i,"")
        print(":->OK.")          
        not_detected_letter_pos.pop(0)
        print(":->Not detected letter and pos...")
        for h,k in enumerate(not_detected_letter_pos):
            print("{}->{}".format(h,k))
        print(":->OK.")
        """------------------------------------------------STOP AUTO FIND POSITION OF NOT RECOGNIZED LETTER--------------------------------------------"""
        """############################################################################################################################ """
        """---------------------------------------------------START ADD LETTER AND HIS POSITION FROM AUTOCMPLETE ALGORITM----------------------"""
        for lo,c in enumerate(not_detected_letter_pos):
            _,x,y,x2,y2 =  not_detected_letter_pos[lo]
            w,h =18,18
            not_detected_letter_pos_dictionary[c[0]] =(x,y,x2,y2,w,h)
        for lo,c in enumerate(not_detected_letter_pos):
            x,y,x2,y2,w,h =not_detected_letter_pos_dictionary[c[0]]
            cx, cy = x+w/2, y+h/2
            cx =cx +7
            cy = cy +7
            imgPt_c = np.array([[cx],[cy],[1 ]])
            worldPt_c = k_inv.dot(depth_cam2key * imgPt_c)
            centroid_dict[c[0]] = (worldPt_c[0,0], worldPt_c[1,0])
            pos_dict[c[0]] =(x,y,x+w,y+h,cx,cy,w,h)
        """---------------------------------------------------STOP ADD LETTER AND HIS POSITION FROM AUTOCMPLETE ALGORITM--------------"""
        """############################################################################################################################ """
        """-------------------------------------------------START TYPING ALGORITM-----------------------------------------------------"""
        """############################################################################################################################ """ 
        cap = cv2.VideoCapture(vide_source)
        print("4===========================================")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        start_send_to_robot  = True 
        while True:
            string_1 = input("Enter a word for the robot arm to type. Letters only. No spaces. Type 'exit' to end program\n").upper()
            if string_1 == "EXIT":
                break
            
            for letter in string:
                start_send_to_robot  = True 
                while True:
                
                    # the loop is used to clear the buffer so that the latest frame will be read by cap.read(). There are 5 buffer frames, according to a forum post. 
                    for i in range(4):
                        cap.grab()
                    
                    ret, frame = cap.read()
                    frame_drawn = frame.copy()
                    letter_keyboard =frame.copy()
                    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    mask_lo = cv2.inRange(frame_hsv, np.array([0,100,130]), np.array([10,255,255]))
                    mask_hi = cv2.inRange(frame_hsv, np.array([175,100,130]), np.array([180,255,255]))
                    mask = cv2.bitwise_or(mask_lo, mask_hi)
                    
                    kernel3 = np.ones((3,3), np.uint8)
                    kernel5 = np.ones((5,5), np.uint8)
                    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel5)
                    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel5)
                    canny = cv2.Canny(mask,1000,500)
                    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                                            param1=1000, param2=11, minRadius=5, maxRadius=35)
                    for index,re in enumerate(pos_letter_list):                       # draw rectangular around recognized letter 
                        letter_name,x,y,w,h = re
                        letter_keyboard  = cv2.rectangle(letter_keyboard ,(int(x),int(y)),(int(x)+int(w),int(y)+int(h)),(0,255,0),3)
                        letter_keyboard  = cv2.putText(letter_keyboard , '{}'.format(letter_name), (int(x),int(y)-2),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255),2)
                    cv2.imshow('contourIM',letter_keyboard)
                    for ind, ke in enumerate(not_detected_letter_pos):                # draw rectangular around not recognized letter
                        letter_name,x1,y1,w1,h1 = ke
                        letter_keyboard  = cv2.rectangle(letter_keyboard ,(int(x1),int(y1)),(int(w1),int(h1)),(0,0,255),3)
                        letter_keyboard  = cv2.putText(letter_keyboard , '{}'.format(letter_name), (int(x1),int(y1)-2),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255),2)
                    cv2.imshow('contourIM',letter_keyboard)           
                    if circles is not None and circles.shape[1]==1:                   # ensure exactly one red circle is found
                        # reduce dimensions and convert the (x, y) coordinates and radius of the circles to integers
                        circles = np.round(circles[0, :]).astype("int")
                        (cir_x, cir_y, cir_r) = circles[0]
                        
                    
                        cv2.circle(frame_drawn, (cir_x, cir_y), cir_r, (0, 255, 0), 1) # draw and show red circle
                        cv2.rectangle(frame_drawn, (cir_x - 1, cir_y - 1), (cir_x + 1, cir_y + 1), (0, 128, 255), -1)

                        rx = pos_dict[letter][0]                                      #get position of recognizet letter to draw rect
                        ry = pos_dict[letter][1]                                      #get position of recognizet letter to draw rect
                        rw = pos_dict[letter][2]                                      #get position of recognizet letter to draw rect
                        rh = pos_dict[letter][3]                                      #get position of recognizet letter to draw rect
                        finish_rx =pos_dict[letter][4]
                        finish_ry =pos_dict[letter][5]
                        cv2.rectangle(frame_drawn ,(int(rx),int(ry)),(int(rw+10),int(rh+10)),(0,0,250),3)
                        #"--Target_Letter->"
                        frame_drawn = cv2.putText(frame_drawn, str("--Target_Letter->"+str(letter)+",Pos(X={:6.2f},Y={:6.2f})".format(centroid_dict[letter][0],centroid_dict[letter][1])), (int(10),int(20)-2),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (55,255,255),2)

                        imgPt_cir = np.array([[cir_x],
                                            [cir_y],
                                            [1]])
                                            
                        # convert from pixel to real-world position in millimeter
                        worldPt_cir = k_inv.dot(depth_cam2cir * imgPt_cir)
                        #Actual terminal point position:,difference between ({}) and robotic arm :
                        frame_drawn = cv2.putText(frame_drawn,(f"Actual terminal point position:(X={int(worldPt_cir[0,0])},Y={int(worldPt_cir[1,0])})"), (int(10),int(50)-2),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (55,255,255),2)
                        frame_drawn = cv2.putText(frame_drawn,("Distance to \"{}\"-:(X={:6.2f}mm,Y={:6.2f}mm)".format(letter,x_diff,y_diff)), (int(10),int(70)-2),cv2.FONT_ITALIC, 0.6, (55,255,255),2)
            
                        start = tuple((cir_x,cir_y))
                        midle = tuple((int(finish_rx),int(cir_y)))
                        finish = tuple((int(finish_rx),int(finish_ry)))

                        cv2.circle(frame_drawn,center=(cir_x,cir_y),radius=5,color=(0,0,255),thickness=5) #Draw circle
                        cv2.line(frame_drawn,(cir_x,cir_y),midle,color=(0,255,0),thickness=2)
                        
                        cv2.circle(frame_drawn,center=midle,radius=5,color=(255,0,0),thickness=5) #Draw circl
                        cv2.line(frame_drawn,midle,finish,color=(0,255,0),thickness=2)
                        
                        cv2.circle(frame_drawn,center=finish,radius=3,color=(0,0,255),thickness=3) #Draw circle
                        cv2.line(frame_drawn,start,finish,color=(255,255,0),thickness=2)
                        # find the difference between the target 'letter' and the red dot 
                        x_diff = centroid_dict[letter][0] - worldPt_cir[0,0]
                        
                        x_diff = -x_diff # negated so that this difference can be directly added to the current robot position
                        y_diff = centroid_dict[letter][1] - worldPt_cir[1,0]
                        # print("x_diff: {:6.2f}, y_diff: {:6.2f}".format(x_diff, y_diff))
                        frame_drawn = cv2.putText(frame_drawn,("Printed Word:->{}".format(printed_text)), (int(10),int(90)-2),cv2.FONT_ITALIC, 0.6, (0,255,0),2)
                        """ --------------------------------------TEST SEND CODE TO ROBOTIC ARM------------------------- """
                        if start_send_to_robot == True:
                            start_send_to_robot = False
                            print(type(string))
                            print("---->>>>{}".format(string))
                            self.type_on_keyboard(letter)
                            cv2.imshow('imgasasd',frame_drawn)
                            cv2.imshow('img2',canny)
                            break
                        """ --------------------------------------FINISH------------------------------------------------ """
                        if abs(x_diff) < 7 and abs(y_diff) <7:
                            start_send_to_robot == True 
                            print("x_diff<0.9")
                            inRange_count += 1
                            if inRange_count == good_inRange_count:  # only allow publishing when the red dot is in range a certain number of times in a row
                                can_publish = True
                            printed_text = printed_text +letter
                            frame_drawn = cv2.putText(frame_drawn,("Printed Word:->{}".format(printed_text)), (int(10),int(90)-2),cv2.FONT_ITALIC, 0.6, (0,255,0),2)
                            cv2.imshow('imgasasd',frame_drawn)
                            break
                        cv2.imshow('imgasasd',frame_drawn)
                        cv2.imshow('img2',canny)
                        
                    elif circles is not None and circles.shape[1]>1:
                        print('more than one red circles are found')
                        
                    elif circles is None:
                        print('no circles are found')
                    
                    if cv2.waitKey(1) == ord('q'):
                        break
            
        
        cv2.destroyAllWindows()
        cap.release()






class MyVideoCapture:
      def __init__(self, video_source=detect_camera_video_source):
          # Open the video source
          print("========Init Video Capture Class=======")
          self.vid = cv2.VideoCapture(video_source)
          if not self.vid.isOpened():
              raise ValueError("Unable to open video source", video_source)
          # Get video source width and height
          self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
          self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
          
  
      def get_frame(self):
          if self.vid.isOpened():
              ret, frame = self.vid.read()
              if ret:
                  return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
              else:
                  return (ret, None)
              return (ret, None)
     # Release the video source when the object is destroyed
      def __del__(self):
          if self.vid.isOpened():
              self.vid.release()   

class Cognitive_Service:
    def __init__(self):
        print("========Init Cognitive Service Class=======")
        self.initialize_cognitive_service()
        self.ku = Function_Treeview()

    def initialize_cognitive_service(self,*args):
        # Add  and verify your Computer Vision subscription key to your environment variables.
        if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
            subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
            print("        ->FIND COMPUTER_VISION_SUBSCRIPTION : OK")
        else:
            print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
            os._exit(1)
        # Add and verify your Computer Vision endpoint to your environment variables.
        if 'COMPUTER_VISION_ENDPOINT' in os.environ:
            endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
            print("        ->FIND COMPUTER_VISION_ENDPOINT : OK")
        else:
            print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
            sys.exit()
        self.computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
        print("        ->FIND COMPUTER_VISION_CLIENT : OK")
        #----------------------------------------------END verify key block------------------------------------------------------------
    
    def recognize_input_text(self,*args,mode_detection,name_photo,photo_url):
        """
        Function Name:def recognize_input_text(self,*args,mode_detection,name_photo,photo_url)
        Description:This function is used to send picture to azure.cognitive.servie for text or object recognition.
                    The funtion return text witch was detected by azure.cognitive.services on the picture.
        Parameteres >>
                    mode_detection =  it means the way of detection like : 1 =Text from board Camera
                                                                           2 =Detect text from URL Photo
                                                                           3 =Object detection /mandatory
        Return>>
              The output of this function is recognizet text 
         """
        global video_terminal
        global name_text_CAMERA_to_detection,detectet_text
        if(mode_detection == 1):
            print("===== Batch Read File - local =====")
            # Get image of handwriting
            foto_name ="frame-"+name_text_CAMERA_to_detection.get()
            local_image_handwritten_path = foto_name+".jpg"
            # Open the image
            local_image_handwritten = open(local_image_handwritten_path, "rb")
            rect_image = cv2.imread(local_image_handwritten_path)
            # Call API with image and raw response (allows you to get the operation location)
            recognize_handwriting_results = self.computervision_client.batch_read_file_in_stream(local_image_handwritten, raw=True)
            # Get the operation location (URL with ID as last appendage)
            operation_location_local = recognize_handwriting_results.headers["Operation-Location"]
            # Take the ID off and use to get results
            operation_id_local = operation_location_local.split("/")[-1]

            # Call the "GET" API and wait for the retrieval of the results
            while True:
                recognize_handwriting_result = self.computervision_client.get_read_operation_result(operation_id_local)
                if recognize_handwriting_result.status not in ['NotStarted', 'Running']:
                    break
                time.sleep(1)
            image = Image.open(local_image_handwritten_path)
            ax = plt.imshow(image)
            # Print results, line by line
            global text_rec
            text_rec = ""
            if recognize_handwriting_result.status == TextOperationStatusCodes.succeeded:
                for text_result in recognize_handwriting_result.recognition_results:
                    for line in text_result.lines:
                        bounding_string=''
                        print(line.text)
                        video_terminal.insert(0.0,">>>"+line.text+"\n")
                        print(line.bounding_box)
                        #////////////////////
                        bbox = [int(num) for num in line.bounding_box]
                        print(bbox)
                        text = line.text
                        text_rec = text_rec+line.text
                        origin = (bbox[0], bbox[1])
                        patch = Rectangle(origin, bbox[2], bbox[3],
                        fill=False, linewidth=2, color='y')
                        ax.axes.add_patch(patch)
                        plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
                        
                        cv2.rectangle(rect_image,(bbox[0],bbox[1]),(bbox[0]+bbox[2],bbox[1]+bbox[3]),(0,255,0),2)
                        if line.text != "":
                            l = len(line.text)*14
                            print("line "+str(l))
                        cv2.rectangle(rect_image,(bbox[0],bbox[3]),((bbox[0]+l-30),bbox[1]-35),(0,255,0),-5)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(rect_image,text,(bbox[0]-50,bbox[1]), font, 0.8,(0,255,0),1,cv2.LINE_AA)
            print("____TEXTUL RECUNOSCTU____->{}".format(text_rec))
            cv2.imshow("image",rect_image)
            cv2.waitKey(0)
            # cv2.destroyAllWindows()
            self.ku.typing_word(string=text_rec)
            detectet_text = text_rec
            #self.ku.type_on_keyboard(word=text_rec)

        if (mode_detection== 2):
            text_rec = ""
            #remote_image_printed_text_url = "https://scontent.fkiv4-1.fna.fbcdn.net/v/t1.15752-9/84260043_876958676100606_8330655606843113472_n.jpg?_nc_cat=104&_nc_sid=b96e70&_nc_ohc=B0zZUy-08FgAX8avM3j&_nc_ht=scontent.fkiv4-1.fna&oh=fc35b2b73169f399f720eab1ff2f0171&oe=5E825E39"
            remote_image_printed_text_url_1 =str(photo_url)
            print("URL FROM ENTRY->"+remote_image_printed_text_url_1)
            # Call API with URL and raw response (allows you to get the operation location)
            recognize_printed_results = self.computervision_client.batch_read_file(remote_image_printed_text_url_1,  raw=True)
            print(recognize_printed_results)
            # Get the operation location (URL with an ID at the end) from the response
            operation_location_remote = recognize_printed_results.headers["Operation-Location"]
            # Grab the ID from the URL
            operation_id = operation_location_remote.split("/")[-1]

            # Call the "GET" API and wait for it to retrieve the results 
            while True:
                get_printed_text_results = self.computervision_client.get_read_operation_result(operation_id)
                if get_printed_text_results.status not in ['NotStarted', 'Running']:
                    break
                time.sleep(1)
            bounding_string =""
            image = Image.open(BytesIO(requests.get(remote_image_printed_text_url_1).content))
            ax = plt.imshow(image, alpha=0.5)
            # Print the detected text, line by line
            text_rec=""
            if get_printed_text_results.status == TextOperationStatusCodes.succeeded:
                video_terminal.insert(0.0,"==========================\n")
                for text_result in get_printed_text_results.recognition_results:
                    for line in text_result.lines:
                        print(line.text)
                        video_terminal.insert(0.0,">>>"+line.text+"\n")
                        print(line.bounding_box)
                        # bounding_string = ' '.join([str(elem) for elem in line.bounding_box]) 
                        # video_terminal.insert(0.0,">>>"+bounding_string+"\n")
                        #////////////////////
                        bbox = [int(num) for num in line.bounding_box]
                        print(bbox)
                        text = line.text
                        text_rec = text_rec+line.text
                        origin = (bbox[0], bbox[1])
                        """ bbox[2]= shirina,bbox[3]=visota """
                        patch = Rectangle(origin, bbox[2], bbox[3],
                        fill=False, linewidth=2, color='g')
                        ax.axes.add_patch(patch)
                        plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
                        print("First bbox[0]="+str(bbox[0]))
                        print(type(bbox[3]))
                        x=int(bbox[0])
                        y=int(bbox[1])
                        w=int(bbox[2])
                        h=int(bbox[3])
                        text_rec = line.text
                        # self.rect(img=image,x=xxx,y=y,w=w,h=h,text="ds")
            detectet_text = text_rec       
            video_terminal.insert(0.0,"======DETECTED TEXT======\n")
            plt.show()
            plt.axis("off")    
            analysis = get_printed_text_results
            print(analysis)

            print()
        if(mode_detection == 3):
            print("===========We are Sorry , this functions is in progress of development==========")
    def rect(self,*args,img,x,y,w,h,text=""):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        if text != "":
            l = len(text)*14
        cv2.rectangle(img,(x,y-22),(x+l,y),(0,255,0),-1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,text,(x,y), font, 0.8,(0,0,0),1,cv2.LINE_AA)
        # cv2.imshow('frame', img)
        # cv2.waitKey(0) & 0xFF
        # cv2.destroyAllWindows()

           
       
if __name__ =="__main__":
    root=Tk()
    funct_tree=Function_Treeview()
    cognitive_class = Cognitive_Service()
    help1=PhotoImage(file="help1.gif")
    home=PhotoImage(file="home.gif")
    zero=PhotoImage(file="reset_main.gif")
    state=PhotoImage(file="state_main.gif")
    return1=PhotoImage(file="return.gif")
    connect=PhotoImage(file="connect.gif")
    disconnect=PhotoImage(file="discon.gif")
    y_up=PhotoImage(file="y.gif")
    y_down=PhotoImage(file="y-down.gif")
    z_up=PhotoImage(file="z-up.gif")
    z_down=PhotoImage(file="z-down.gif")
    x_up=PhotoImage(file="x-up.gif")
    en_flag = PhotoImage(file="en.gif")
    rom_flag = PhotoImage(file = "rom.gif")
    x_down=PhotoImage(file="x-down.gif") 
    send=PhotoImage(file="send.gif")
    rus_flag = PhotoImage(file="rus.gif")
    manual_control_gif=PhotoImage(file="manual_control_black.gif")
    text_recognition_gif=PhotoImage(file="text_recognition.gif")
    comand=Arduino_Control(root)
    root.mainloop()
 

#  import requests

# url = 'https://app.nanonets.com/api/v2/OCR/Model/8158ef6f-7d10-4d9c-bd91-224fbc5b2bbc/LabelFile/'

# data = {'file': open('REPLACE_IMAGE_PATH.jpg', 'rb')}

# response = requests.post(url, auth=requests.auth.HTTPBasicAuth('41gA5w2Yx_a6T4GKsMPegkZZITqwQ4EW', ''), files=data)

# print(response.text)