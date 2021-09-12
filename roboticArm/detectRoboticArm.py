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

distance = 0
print(":->Init program variables...")
"""############################################################################################################################ """
"""--------------------------------------Define all variable and constant----------------------------------------- """
x_diff = 0
y_diff = 0
ii = 0
input_shape = (30,30,1)
num_classes = 61
vide_source = 1
x,y,w,h,cx,cy = 0,0,0,0,0,0
centroid_dict = {}
pos_dict = {}
global pos_letter_list
pos_letter_list= [(0,0,0,0,0)]
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
inRange_count = 0
can_publish = False
printed_text =" "
### (end) Inputs ---------------------------------------------------------------------------------------
"""--------------------------------------END-Define all variable and constant----------------------------------------- """
"""############################################################################################################################ """
"""--------------------------------------NEURONAL NETWORK INITIALIZE----------------------------------------- """
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

print(":->OK.")
cap = cv2.VideoCapture(vide_source)
# print("\nWhen the video shows that all the letters are boxed in, select the video window and press 'q'")
print(":->Start automate detection of letter from keyboard...")
image_good = False
"""############################################################################################################################ """
"""--------------------------------------START AUTOMATE DETECTION OF LETTER FROM KEYBOARD AND SEND IT TO CNN----------------------------------------- """

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
        for i,(x,y,w,h) in enumerate(contours_bb):                                # (x,y) is the top left corner of the box
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
            char_img = char_img/255*2 -1                                           #shape is now (30,30)
            char_img = np.expand_dims(char_img, axis=0)                            #shape is now (1,30,30)
            char_img = char_img[..., np.newaxis]                                   #shape is now (1,30,30,1)
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
        if ii>=23:
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
#save gray format
cv2.imwrite("Original.jpg",frame)
cv2.imwrite("Grey.jpg",gray)
cv2.imwrite("threshold.jpg",threshold)
cv2.imwrite("mask.jpg",mask)
cv2.imwrite("char_img.jpg",char_img)
cv2.imwrite("contourIM.jpg",contourIM)
print("--------Save")
print(":->OK.")   
cv2.destroyAllWindows()
cap.release()
cap_2 = cv2.VideoCapture(vide_source)
print(":->Transform detected letter from 3D to 2D...")
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
string = "sdfsfsfs"
"""---------------------------------------------------STOP ADD LETTER AND HIS POSITION FROM AUTOCMPLETE ALGORITM--------------"""
"""############################################################################################################################ """
"""-------------------------------------------------START TYPING ALGORITM-----------------------------------------------------"""
"""############################################################################################################################ """ 
cap = cv2.VideoCapture(vide_source)
print("---->>>{}".format(detectet_letter))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    word = input("Enter a word for the robot arm to type. Letters only. No spaces. Type 'exit' to end program\n").upper()
    if word == "EXIT":
        break
    
    for letter in word:
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
                if abs(x_diff) < 7 and abs(y_diff) <7:
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

