from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")


        #label 
        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_Top=Image.open(r"train3.jpg")
        img_Top=img_Top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_Top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        #button 
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor='hand2',font=("times new roman",30,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"train4.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      #Grey scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ==========Training the Classfier================


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("final_data.xml")
        cv2.destroyAllWindows()   
        messagebox.showinfo("Result","Training dataset completed !!")                                                           
 
        

 
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()