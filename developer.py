from cProfile import label
from cgitb import handler
from ctypes.wintypes import HANDLE
from logging import exception
from sre_parse import State
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from turtle import title, width
from PIL import Image,ImageTk
from matplotlib.pyplot import text
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #label 
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_Top=Image.open(r"dev1.jpg")
        img_Top=img_Top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_Top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=300)

        #developer info
        dev_label=Label(main_frame,text="Hello from our side. We're Amit, Sahil, Harsh and Shreyansh",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="We are in our Final Year",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Email: identix@mitaoe.ac.in",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=80)


if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()       