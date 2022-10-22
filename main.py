from cgitb import handler
from ctypes.wintypes import HANDLE
from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import Image,ImageTk
from setuptools import Command
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os



class Face_Recognition_system:
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")
        #first image 
        img=Image.open(r"D:\Major project\Facial-Recognition-System_new.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image 
        img1=Image.open(r"D:\Major project\925-9258920_3d-depth-perception-color-texture-analysis-d-id.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=500,y=0,width=550,height=130)
        
        #3rd image  
        img2=Image.open(r"D:\Major project\Facial-Recognition-System_new.png")
        img2=img2.resize((500,130),Image.ANTIALIAS) 
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg image
        img3=Image.open(r"D:\Major project\istockphoto-1310822232-170667a.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)
         
        #label 
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTEDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # student button
        img4=Image.open(r"studentdetails.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)

        # detect face button
        img5=Image.open(r"facedetector.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimage5,cursor='hand2',command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor='hand2',command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendance face button
        img6=Image.open(r"attendance1.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimage6,command=self.student_details,cursor='hand2')
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help Desk button
        img7=Image.open(r"helpdesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimage7,command=self.student_details,cursor='hand2')
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Train face button
        img8=Image.open(r"facetrain.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimage8,cursor='hand2',command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Face",cursor='hand2',command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Photos face button
        img9=Image.open(r"photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimage9,cursor='hand2',command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor='hand2',command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=500,y=580,width=220,height=40)

        # Developer button
        img10=Image.open(r"developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimage10,command=self.student_details,cursor='hand2')
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)

        # exit button
        img11=Image.open(r"D:\Major project\photo-1559284379-46ac083d4028.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        
        self.photoimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimage11,command=self.student_details,cursor='hand2')
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    # =============function butttons=============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        

    


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()