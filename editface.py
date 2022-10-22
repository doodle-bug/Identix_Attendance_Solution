from itertools import Predicate
from pyexpat import features
from tkinter import*
from tkinter import ttk
from turtle import width
from time import strftime
from  datetime import date, datetime
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        #label
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_Top=Image.open(r"C:\Users\91902\Desktop\face_attendance\What-is-Synthetic-Data_-2.png")
        img_Top=img_Top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_Top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl=Place(x=0,y=55,width=1530,height=700)

        img_bottom=Image.open(r"C:\Users\91902\Desktop\face_attendance\1_Hmqbvj-Y5jCkz5-53o8G_g.jpeg")
        imgbottom=img_bottom.resize((900,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl=Place(x=650,y=55,width=900,height=700)


        #button 
        b1_1=Button(f_lbl.root,text="Face Recognition",cursor='hand2',font=("times new roman",18,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=360,y=620,width=200,height=40)

        #### attendance ### 
    def mark_attendance(self,i,r,d,S): 
        with open("sahil.csv","r+",newline="\n") as f:  
            mydatalist=f.readline()
            name_list=[]
            for line in mydatalist:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list)) and ((r not in name_list)) and ((d not in name_list)) and ((S not in name_list)):
                now=datetime.now(0)
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{S},{dt},{d1},Preset")

##########3 face recognition ########33
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cv2Color(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Major@123")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Name from Student_id where Student_id="+str(id))
                S=my_cursor.fetchone()
                S="+".join(S)


                if confidence>77:
                    cv2.putText(img,f"ID:{S}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,S,d )
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  
                
                coord=[x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifer("# harcascade")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()







if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()