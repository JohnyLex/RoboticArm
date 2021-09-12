from tkinter import *
import time
from functools import partial
import serial
color_label ='yellow'
send_1 ="G90 G21"
ser = serial.Serial(
        port='COM3',
        baudrate =115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
class Function:
    def __init__(self):
        print("init")
    def printw(self): 
        print("test connection fynctio")
    def image_loader(self,value):
        if value == 1:
            help1=PhotoImage(file="help1.gif")
            return help1
        if value == 2:
            home=PhotoImage(file="home.gif")
            return home
        if value == 3: 
            zero=PhotoImage(file="reset_main.gif")  
            return zero
        if value == 4:
            state=PhotoImage(file="state_main.gif")
            return state
        if value  ==5:
            return1=PhotoImage(file="return.gif")
            return return1
        if value ==6:
            connect=PhotoImage(file="connect.gif")
            return connect
        if value ==7:
            disconnect=PhotoImage(file="discon.gif")
            return disconnect
        if value ==8:
            y_up=PhotoImage(file="y.gif")
            return y_up
        if value ==9:
            y_down=PhotoImage(file="y-down.gif")
            return y_down
        if value ==10:
            z_up=PhotoImage(file="z-up.gif")
            return z_up
        if value ==11:
            z_down=PhotoImage(file="z-down.gif")
            return z_down
        if value ==12: 
            x_up=PhotoImage(file="x-up.gif")
            return x_up
        if value ==13:
            x_down=PhotoImage(file="x-down.gif")
            return x_down
        if value ==14:
            send=PhotoImage(file="send.gif")
            return send


class Arduino_Control(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.fun = Function()
        self.create_widgets()
        self.window_config()
        self.initMainMenu()
    
    def window_config(self):
        self.master.title("Test Gcode Sender by Lex v1.0")
        self.master.geometry("1000x800+400+120")
    
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

        self.stepOne =LabelFrame(self, text="Common Actions ")
        self.stepOne.grid(row=1, columnspan=10, sticky='W',padx=7, pady=5, ipadx=5, ipady=5)

        self.monitoring =LabelFrame(self, text=" Status Real Time Block  ")
        self.monitoring.grid(row=2, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

        self.buzzer_control = LabelFrame(self,text="Conection Control")
        self.buzzer_control.grid(row=0,column=0,columnspan=10,sticky='W',padx=7,pady=5,ipadx=5,ipady=5)

        self.terminal_frame = LabelFrame(self,text="Real Time Terminal")
        self.terminal_frame.grid(row=0, column=7, columnspan=2, rowspan=10,sticky='NS', padx=5, pady=5)
        self.send_comand_frame = LabelFrame(self,text="Send Comand")
        self.send_comand_frame.grid(row=30, column=8, columnspan=2, rowspan=20,sticky='NS', padx=5, pady=5)

        self.robotic_frame =LabelFrame(self, text=" Robotic Arm Control Block  ")
        self.robotic_frame.grid(row=3, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        self.entry_gcode_comands=Entry(self.send_comand_frame,width=50)
        self.entry_gcode_comands.grid(row=0,column =0)

        self.set_position_label =LabelFrame(self,text="Work Set Position")
        self.set_position_label.grid(row=5, columnspan=8, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        self.actual_position =LabelFrame(self,text="Actual  Position")
        self.actual_position.grid(row=5, column=3, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        #work position block
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
        
        
        self.get_state_button  = Button(self.stepOne,text="Get State",command=self.set_on_led,image=state,borderwidth=0).grid(row=0, columnspan=2,sticky=W,padx=5,pady=5,)
        self.rt_zero_button = Button(self.stepOne,text="Return to Zero",command=self.set_off_led,image=return1,borderwidth=0 ).grid(row=0,column=2,sticky=W,padx=5,pady=5,)
        self.reset_zero_button= Button(self.stepOne,text="Reset to Zero",command=self.set_on_led,image=zero,borderwidth=0 ).grid(row=1, columnspan=2,sticky=W,padx=5,pady=5,)
        self.home_machine_button = Button(self.stepOne,text="Home Machine",command=self.set_off_led,image=home,borderwidth=0 ).grid(row=1,column=2,sticky=W,padx=5,pady=5,)
        self.buz_on_button  = Button(self.buzzer_control,text="Connect",command=self.connect,image=connect,borderwidth=0).grid(row=0, columnspan=2,sticky=W,padx=5,pady=5,)
        self.buz_off_button = Button(self.buzzer_control,text="Disconnect",command=self.disconect,image=disconnect,borderwidth=0).grid(row=0,column=2,sticky=W,padx=5,pady=5,)
        self.home_machine_button = Button(self.stepOne,text="Help",command=self.set_off_led,image=help1, borderwidth=0 ).grid(row=3,column=0,sticky=W,padx=5,pady=5,)

        self.answer=Text(self.monitoring, width=15, height=1, wrap=WORD)
        self.answer.grid(row=4, column=1, sticky=W)
        self.textBox7 = Text(self.monitoring,height=1,width=17)
        self.textBox7.grid(row=3,column=1)


        self.arm_left =Button(self.robotic_frame,image=x_down,borderwidth=0,command=partial(self.callback,3)).grid(row=2,column=0, sticky=W)
        self.arm_up =Button(self.robotic_frame,image =y_up ,borderwidth=0,command=partial(self.callback,1))
        self.arm_up.grid(row=1,column=1, sticky=W)
        self.arm_left =Button(self.robotic_frame,image =x_up ,borderwidth=0,command=partial(self.callback,4)).grid(row=2,column=2, sticky=W)
        self.arm_up =Button(self.robotic_frame,image=y_down,borderwidth=0,command=partial(self.callback,2)).grid(row=3,column=1, sticky=W)

        self.arm_left =Button(self.robotic_frame,image=z_down,borderwidth=0,command=partial(self.callback,6)).grid(row=1,column=3, sticky=W)
        self.arm_up =Button(self.robotic_frame,image =z_up ,borderwidth=0,command=partial(self.callback,5)).grid(row=3,column=3, sticky=W)
        
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
        self.text1 = Text(self.terminal_frame, height=40, width=55)
        self.scroll = Scrollbar(self.terminal_frame, command=self.text1.yview, orient=VERTICAL, width=30 )
        self.scroll.config(command=self.text1.yview)
        self.text1.grid(row=0,column=0,sticky=W)
        self.scroll.grid(row=0,column=1,sticky=E)
        #STOP----------------------------------------------------------
        #command=self.send_command(self.entry_gcode_comands.get())
        
        
        self.send_button = Button(self.send_comand_frame,image=send,command=self.send_command,borderwidth=0).grid(row=0,column=1,sticky=W,padx=5,pady=5)
        
    def onreturn(self):
        print("b")
    
    def connect(self):
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
            self.answer.insert(0.0,"G21G91-Y"+xy+"F"+feed+"\n")
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
            self.answer.insert(0.0,"G21G91-X"+xy+"F"+feed+"\n")
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
            self.answer.insert(0.0,"G21G91-Z"+z+"F"+feed+"\n")
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
        







        
       
if __name__ =="__main__":
    root=Tk()
    funct=Function()
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
    x_down=PhotoImage(file="x-down.gif")
    send=PhotoImage(file="send.gif") 
    comand=Arduino_Control(root)
    root.mainloop()

