from tkinter import *  
from tkinter import ttk 
import time
from functools import partial

import tkinter

class Arduino_Control(Frame):
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
        self.video_recognition_main_label=LabelFrame(self.Text_Recognition_Block, text="Video Recognition") #done
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
  
        self.export=Button(self.Main_Detection_Label,text="Export as...",borderwidth=1).grid(row=1,column=0, sticky=W,padx=5,pady=5)
        self.delete=Button(self.Main_Detection_Label,text="Delete row",borderwidth=1,command=self.intermediate_delete_selectet_treeview).grid(row=1,column=1, sticky=W,padx=5,pady=5)
        self.print_text=Button(self.Main_Detection_Label,text="Type on keyboard",borderwidth=1,command = self.intermediate_detect_type_on_keyboard).grid(row=1,column=2, sticky=W,padx=5,pady=5)

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

        


    def video_frame(self):
        # Create a canvas that can fit the above video source size
        global Video_Frame_Label
        
        self.canvas = Canvas(self.Video_Detection_Label, width = self.vid.width, height = 350)
        print(self.vid.width) 
        self.canvas.grid(row=0,column=0)
        # Button that lets the user take a snapshot
        self.btn_snapshot=Button(self.Main_Detection_Label, text="Snapshot", width=10, command=self.snapshot)
        self.btn_snapshot.grid(row=1,column=3)
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
        #ser.write(sa+"\n")
        #self.grbl_out=ser.readline()
        #print(":"+self.grbl_out.strip())
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
            xyy = -xy
            self.answer.insert(0.0,"G21G91X"+(xyy)+"F"+feed+"\n")
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
            z1 = -z
            self.answer.insert(0.0,"G21G91Z"+z1+"F"+feed+"\n")
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
        print("999999999999999999999999999999")
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.master.after(self.delay, self.update)
        