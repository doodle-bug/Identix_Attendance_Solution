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



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #label 
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_Top=Image.open(r"hd2.png")
        img_Top=img_Top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_Top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email: identix@mitaoe.ac.in",font=("times new roman",30,"bold"),bg="white")
        dev_label.place(x=550,y=100)


if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()       